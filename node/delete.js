var db = require('riak-js').getClient({
  pool: {
    servers: ['bdc-n-e3.fbi.h-da.de:8098', 'bdc-n-e4.fbi.h-da.de:8098']
  }
});
/*var db = require('riak-js').getClient({
  host: 'bdc-n-e4.fbi.h-da.de', port: '8098', debug: true
});*/

var total = 0;

var instrument = {
  'riak.request.start': function(event) {
    //console.log('[riak-js] [start] ' + event.method.toUpperCase() + ' ' + event.path);
  },
  'riak.request.end': function(event) {
    //console.log('[riak-js] [end] ' + event.method.toUpperCase() + ' ' + event.path);
    total++;
  }
};

db.registerListener(instrument);

var args = process.argv.splice(2);
var bucket = args[0] || 'testicals';

// stupid strange workaround... too tired -_-
var test = [];

db.keys(bucket, { keys: 'stream' }).on('keys', function(keys) {
  for (var key in keys) {
    test.push(keys[key]);
  }
}).start();

setInterval(function() {
  if (test.length !== 0) {
    db.remove(bucket, test.pop());
  }
  if (total % 1000 === 0 && total !== 0) {
    console.log("Already deleted " + total + " data sets...");
  }
}, 1);
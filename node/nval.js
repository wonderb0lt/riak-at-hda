var db = require('riak-js').getClient({
  host: 'bdc-n-e3.fbi.h-da.de', port: '8098', debug: true
});

var args = process.argv.splice(2);
var bucket = args[0];

db.saveBucket(bucket, {n_val: 3, allow_mult: true}, function(err, data) {
  if (err) {
    console.log(err);
  }
});
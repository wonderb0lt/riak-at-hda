var db = require('riak-js').getClient({
  pool: {
    servers: ['bdc-n-e3.fbi.h-da.de:8098', 'bdc-n-e4.fbi.h-da.de:8098']
  },
  debug: true
});

var args = process.argv.splice(2);
var bucket = args[0];

db.count(bucket, function (err, data) {
  console.log("Key count: " + data);
  process.exit();
});
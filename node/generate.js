var _ = require('underscore');
var genie = require('./genie');
var db = require('riak-js').getClient({
  pool: {
    servers: ['bdc-n-e3.fbi.h-da.de:8098', 'bdc-n-e4.fbi.h-da.de:8098']
  }
});
/*var db = require('riak-js').getClient({
  host: 'bdc-n-e3.fbi.h-da.de', port: '8098', api: 'protobuf'
});*/

var requests = 0;
var index = 0;

var MAX_REQUESTS = 100;

var instrument = {
  'riak.request.start': function(event) {
    console.log('[riak-js] [start] ' + event.method.toUpperCase() + ' ' + event.path);
    requests++;
  },
  'riak.request.end': function(event) {
    console.log('[riak-js] [end] ' + event.method.toUpperCase() + ' ' + event.path);
    requests--;
  }
}

db.registerListener(instrument);

var start = process.hrtime();

var elapsed_time = function(note) {
  var precision = 3; // 3 decimal places
  var elapsed = process.hrtime(start)[1] / 1000000; // divide by a million to get nano to milli
  console.log(process.hrtime(start)[0] + " s, " + elapsed.toFixed(precision) + " ms - " + note); // print message + time
  start = process.hrtime(); // reset the timer
}

var companies = ['Aeroflot', 'Air France', 'German Wings', 'Air Berlin', 'Lufthansa', 'Aer Lingus',
    'US Airways', 'Delta Airlines'
];
var destinations = [{
    "country": "France",
    "city": "Paris",
    "iata": "ORY",
    "airport": "Orly Arpt",
    "terminals": ["W"]
  }, {
    "country": "France",
    "city": "Montpellier",
    "iata": "MPL",
    "airport": "Frejorgues Arpt",
    "terminals": []
  }, {
    "country": "Germany",
    "city": "Munich",
    "iata": "MUC",
    "airport": "Munich Intl Arpt",
    "terminal": "2"
  }, {

    "country": "Germany",
    "city": "Dusseldorf",
    "iata": "DUS",
    "airport": "Dusseldorf Arpt",
    "terminal": ""
  }, {
    "country": "France",
    "city": "Toulouse",
    "iata": "TLS",
    "airport": "Blagnac Arpt",
    "terminal": ""
  }, {
    "country": "Thailand",
    "city": "Bangkok",
    "iata": "BKK",
    "airport": "Suvarnabhumi Intl Arpt",
    "terminal": ""
  }
];
var aircrafts = ['Airbus A380', 'Boeing 747', 'Airbus A320-200'];

var flightTemplate = {
  "id": {
    format: '##.#.#'
  },
  "personalFlightData": {
    max: 2,
    template: {
      eTicket: {
        format: '############C#'
      },
      "class": {
        oneOf: [
            'Economy',
            'First Class'
        ]
      },
      baggage: {
        format: 'ADT #PC'
      }
    }
  },
  "passengers": {
    max: 1,
    template: {
      "type": {
        format: '0'
      },
      "name": {
        pattern: 'firstName'
      },
      "surname": {
        pattern: 'lastName'
      },
      "id": function() {
        return this.name.toUpperCase() + '/' + this.surname.toUpperCase();
      }
    }
  },
  "flights": {
    min: 1,
    max: 4,
    template: {
      "id": {
        format: '..####',
      },
      "departure": function() {
        return Date.now() + 86400000 * _.random(0, 6);
      },
      "arrival": function() {
        return this.departure + 6 * _.random(30, 480);
      },
      "company": {
        oneOf: companies
      },
      "from": {
        oneOf: destinations
      },
      "to": {
        oneOf: destinations
      },
      "duration": function() {
        return this.arrival - this.departure;
      },
      "status": {
        oneOf: [
            'confirmed',
            'unconfirmed',
            'TERRORIST'
        ]
      },
      "aircraft": {
        oneOf: aircrafts
      }
    }
  },
  "fares": {
    template: {
      "type": function() {
        return 'ADT';
      },
      "fop": function() {
        return 'invoice'
      },
      "base": {
        range: [40, 200],
        places: 2
      },
      "taxes": {
        range: [10, 130],
        places: 2
      },
      total: function() {
        return this.base + this.taxes;
      },
      "currency": function() {
        return 'EUR';
      }
    }
  }
};

var args = process.argv.splice(2);
var amount = Number(args[0]) || 1;
var upload = Boolean(args[1]) || false;
var bucket = args[2];

if (args.length < 3) {
  console.log("USE: node generate [amount] [upload] [bucket] > [logfile]");
  console.log("     node generate 1000 true TestBucket > generate.log");
  process.exit();
}

console.log("Generating " + amount + " data sets...");

function generateData() {
  var flight = genie(flightTemplate);

  var segment = '1';
  for (var j = 1; j < flight.flights.length; j++) {
    var newSegment = j + 1;
    segment += ', ' + newSegment;
  };
  flight.fares.segment = segment;

  if (!upload) {
    console.dir(flight);
  } else {
    db.save(bucket, flight.id, flight);
  }

  if (index % 100 === 0) {
    console.log("Generated already " + index + " data sets...");
  }

  index++;
}

// checks that we don't overwhelm the server with requests
function checkRequests() {
  if (index < amount) {
    if (requests < MAX_REQUESTS) {
      generateData();
    } else {
      console.log("I have to wait for reqs to finish...");
    }
  } else {
    console.log("Finally finished...");
    process.exit();
  }
};

process.on('exit', function() {
  elapsed_time('Execution time for: ' + amount + ' data sets.');
});

process.on('SIGINT', function() {
  process.exit();
});

// start the whole mess
setInterval(checkRequests, 10);
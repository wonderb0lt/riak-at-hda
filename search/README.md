# Patrick's marvelous search script

## Installation
Analogous to the [insert installation guide](https://github.com/wonderb0lt/riak-at-hda/blob/master/insert/README.md)

## Usage
To run only a map-query: `./search.py map.js`
To run a map/reduce query: `./search.py map.js reduce.js`

Usually, the map file ends with -map.js, and the reduce file ends with -red.js.

## Existing query files
`avg-map.js` + `avg-red.js` => Average of all taxes in the fares
`begins-in-dusseldorf-objects-map.js` => JSON of all flights starting in Düsseldorf
`begins-in-dusseldorf-map.js` + `begins-in-dusseldorf-red.js` => Count of all flights starting in Düsseldorf
`direct-flights-map.js` => IDs of all direct flights
`no-fares-map.js` => IDs of all flights not payed yet
`one-way-map.js` => IDs of all flights that are one-way.
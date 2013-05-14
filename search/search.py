#!/usr/bin/env python2
'''The search script
Usage: search.py [--buckets=FlightData] <map-file> [<reduce-file>]

Arguments:
  <map-file>  The mapping file (Javascript)
  <reduce-file>  The reduce file (Javascript)

Options:
  --buckets BUCKETS  A list of buckets to use, seperated by commas or just one [default: FlightData]

Examples:
  ./search.py queries/no-fares-map.js # Map only
  ./search.py queries/begins-in-dusseldorf-map.js queries/begins-in-dusseldorf-red.js MapReduce
  ./search.py queries/one-way-map.js --buckets=FlightData  # Buckets specified
'''

from docopt import docopt
import riak
import conf
import os.path
import time

verbose = False

def get_query_string(f):
	if not f or not os.path.exists(f):
		raise ValueError('Given Query file does not exist')
	else:
		with open(f, 'r') as handle:
			return handle.read()

def main(args):
	m = get_query_string(args['<map-file>'])
	
	if args['<reduce-file>']:
		r = get_query_string(args['<reduce-file>'])
	else:
		r = None


	client = riak.RiakClient(host=conf.host, port=conf.port)

	# Add buckets from the command line
	for bucket in args['--buckets'].split(','):
		query = client.add(bucket)

	# Then, you supply a Javascript map function as the code to be executed.
	query.map(m)

	if r:
		query.reduce(r)

	start = time.time()
	results = query.run()
	end = time.time()

	if verbose:
		print 'map: %s' % m
		print 'red: %s' % r

		print 'Querying %s@%s:%d' % (args['--buckets'], conf.host, conf.port)

	print 'Query perfomed successfully! Took %.2fs.' % (end-start)
	print '#### RESULT ####'
	for result in query.run():
	    # Print the key (``v.key``) and the value for that key (``data``).
		print str(result)

if __name__ == '__main__':
	main(docopt(__doc__))
#!/usr/bin/env python2
''' The search script
Usage:
	search.py <map-file> [<reduce-file>]
'''

from docopt import docopt
import riak
import conf
import os.path


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
	client = riak.RiakClient(host='bdc-n-e3.fbi.h-da.de', port=8098)

	# First, you need to ``add`` the bucket you want to MapReduce on.
	query = client.add('FlightData')
	# Then, you supply a Javascript map function as the code to be executed.
	query.map(m)

	if r:
		query.reduce(r)

	for result in query.run():
	    # Print the key (``v.key``) and the value for that key (``data``).
		print str(result)

if __name__ == '__main__':
	main(docopt(__doc__))
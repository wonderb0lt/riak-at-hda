#!/usr/bin/env python2
"""Patrick's awesome insert script!

Usage:
        insert.py (--generate | <file>...)

Options:
    --generate      Generate test data
"""


import sys
import json
import riak
import generate
from docopt import docopt
import uuid
import conf
import stopwatch

def get_data_from_file(files):
    if len(files) == 0:
#        usage()
        sys.exit(2)
    else:
        result = []
        for jsonf in files:
            try:
                with open(jsonf, 'r') as handle:
                    result.append(json.loads(handle.read()))
            except IOError as e:
                print 'Could not read file %s: %s' % (jsonf, str(e))
                sys.exit(1)

        return result

def generate_data():
    print 'Generating %d entries...' % conf.generation['number_of_entries']
    
    for i in xrange(conf.generation['number_of_entries']):
        yield generate.generate_entry()[1]

def main(args):
    if args['<file>']:
        data = get_data_from_file(args['<file>'])
        total = len(data)
    else:
        data = generate_data()
        total = conf.generation['number_of_entries']

    print 'Connecting to Riak...'
    client = riak.RiakClient(host=conf.host, port=conf.port)
    bucket = client.bucket(conf.buckets['flights'])

    insert_timer = stopwatch.Timer()
    for idx, flight in enumerate(data):
        if not args['--generate']:
            print 'Inserting new data for key %s' % flight['id']
        else:
            if idx != 0 and idx % 500 == 0:
                print 'Inserted %.2f%% of all entries...' % float((float(idx) / float(total))*100)

        bucket.new(flight['id'], flight).store()

    print 'Insertion took %.2f seconds' % insert_timer.elapsed
    insert_timer.stop()
    print 'I\'m done.'


if __name__ == '__main__':
    main(docopt(__doc__))

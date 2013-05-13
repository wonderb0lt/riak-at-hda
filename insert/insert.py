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
from docopt import docopt
import uuid
import conf


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


def main(args):
    if args['<file>']:
        data = get_data_from_file(args['<file>'])
    else:
        data = []

    print 'Connecting to Riak...'
    client = riak.RiakClient(host=conf.host, port=conf.port)
    bucket = client.bucket(conf.buckets['flights'])

    for flight in data:
        print 'Inserting new data for key %s' % flight['id']
        bucket.new(flight['id'], flight).store()

    print 'I\'m done.'


if __name__ == '__main__':
    main(docopt(__doc__))

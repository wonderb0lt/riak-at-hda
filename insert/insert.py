#!/usr/bin/env python2
import sys
import json
import riak
import uuid
import conf


def usage():
    print 'Usage: insert.py jsonfile[, jsonfile[, jsonfile[, ...]]]'


def get_data(args):
    if len(args) == 0:
        usage()
    else:
        result = []
        for jsonf in args:
            try:
                with open(jsonf, 'r') as handle:
                    result.append(json.loads(handle.read()))
                    data = open(args[0], 'r').read()
            except IOError as e:
                print 'Could not read file %s' % args[0], e
                sys.exit(1)

        return result


def main(args=[]):
    data = get_data(args)
    print 'Connecting to Riak...'
    client = riak.RiakClient(host=conf.host, port=conf.port)
    bucket = client.bucket(conf.buckets['flights'])

    for flight in data:
        print 'Inserting new data for key %s' % flight['id']
        bucket.new(flight['id'], flight).store()

    print 'I\'m done.'


if (__name__ == '__main__'):
    main(sys.argv[1:])

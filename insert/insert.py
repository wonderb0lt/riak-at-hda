#!/usr/bin/python
import sys
import json
import riak

import conf


def usage():
    print "Usage: insert.py jsonfile"


def get_data(args):
    try:
        data = open(args[0], 'r').read()
    except IOError as e:
        print "Could not read file %s" % args[0], e
        sys.exit(1)
    except IndexError:
        usage()
        sys.exit(2)

    return json.loads(data)


def main(args=[]):
    data = get_data(args)
    client = riak.RiakClient(host=conf.host, port=conf.port)

    # For the first version of this script, we will assume that we save the
    # complete flight data in one single big bucket.
    #
    # We really shouldn't do that.
    flights = client.bucket(conf.buckets['flights'])
    flights.new(data['id'], data=data).store()


if (__name__ == '__main__'):
    main(sys.argv[1:])

#!/usr/bin/python
import sys
import json
import riak
import uuid
import conf


def usage():
    print('Usage: insert.py jsonfile')


def get_data(args):
    if '006MME' not in args[0]:
        print 'Only 006MME.json is already in new format. Sorry.'
        sys.exit(42)


    try:
        data = open(args[0], 'r').read()
    except IOError as e:
        print 'Could not read file %s' % args[0], e
        sys.exit(1)
    except IndexError:
        usage()
        sys.exit(2)

    return json.loads(data)

def insert_booking(client, data):
    print "Storing booking with id %s" % data['booking']['id']
    client.bucket('booking').new(data['booking']['id'], data=data['booking']).store()

def insert_passengers(client, data):
    b = client.bucket('passenger')
    ids = []
    for passenger in data['passengers']:
        key = uuid.uuid1().hex
        print "Storing passenger with random id %s and logical id %s" % (key, passenger['id'])
        b.new(key, passenger).store()
        ids.append(key)

    return ids

def insert_airports(client, data):
    b = client.bucket('airports')

    for key, airport in data['airports'].items():
        print "Storing airport with key %s (name: %s)" % (key, airport['airport'])
        b.new(key, airport).store()

def insert_flights(client, data):
    b = client.bucket('flights')

    for key, flightdata in data['flights'].items():
        print "Storing flight %s (from %s to %s)" % (key, flightdata['from'], flightdata['to'])
        b.new(key, flightdata).store()

def insert_personalflightdata(client, data):
    b = client.bucket('personalflightdata')

    for key, fdata in data['personalflightdata'].items():
        print "Storing personal data with composite key %s" % key
        b.new(key, fdata).store()

def insert_fares(client, data):
    b = client.bucket('fares')
    key = uuid.uuid1().hex

    print 'Inserting fare with random id %s' % key
    b.new(key, data['fares']).store()

    return [key]

def main(args=[]):
    print('Starting...')
    data = get_data(args)
    client = riak.RiakClient(host=conf.host, port=conf.port)

    passenger_ids = insert_passengers(client, data)
    insert_airports(client, data)
    insert_flights(client, data)
    insert_personalflightdata(client, data)
    fare_ids = insert_fares(client, data)

    data['booking']['fares'] = fare_ids

    insert_booking(client, data)

if (__name__ == '__main__'):
    main(sys.argv[1:])

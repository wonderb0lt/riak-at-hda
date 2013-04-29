#!/usr/bin/python
import sys
import json
import riak
import uuid
import conf


def usage():
    print('Usage: insert.py jsonfile')


def get_data(args):
    try:
        data = open(args[0], 'r').read()
    except IOError as e:
        print 'Could not read file %s' % args[0], e
        sys.exit(1)
    except IndexError:
        usage()
        sys.exit(2)

    return json.loads(data)

def insert_airport_for_flight(client, flight):
    airports = client.bucket(conf.buckets['airports'])

    for k in ['from', 'to']:
        flight_data = flight[k]
        iata = flight_data['iata']
        airport = airports.get(iata)

        if not airport.exists():
            print 'Storing Airport %s' % iata
            airports.new(iata, data=flight_data).store()
        else:
            print('Airport %s exists, location: "%s"' % (iata, flight_data['city']))
        # We saved it in a bucket, replace it with a reference.
        flight_data[k] = iata


def insert_flight(client, flight):
    flights = client.bucket(conf.buckets['flights'])

    f = flights.get(flight['id'])
    if not f.exists():
        print 'Inserting flight %s' % flight['id']
        insert_airport_for_flight(client, flight)
        flights.new(flight['id'], data=flight).store()
    else:
        print "Flight with id %s already exists" % flight['id']
def insert_passenger(client, passenger):
    name_array = passenger.keys()[0].split(' ')
    name, surname = name_array[-1], ' '.join(name_array[0:-1])
    key = uuid.uuid1().hex

    passengers = client.bucket(conf.buckets['passengers'])

    print 'Inserting passenger "%s,%s" with random key %s' % (name, surname, key)
    passengers.new(key, {'PassengerID': key, 'Surename': surname, 'name': name}).store()

    return key

def insert_fare_infos(client, fare_info):
    fares = client.bucket(conf.buckets['fares'])

    key = uuid.uuid1().hex
    print "Inserting fare info with random id %s" % key
    fares.new(key, data=fare_info).store()

    return key

def main(args=[]):
    print('Starting...')
    data = get_data(args)
    client = riak.RiakClient(host=conf.host, port=conf.port)

    random_ids = [] # TODO pythonize
    for passenger in data['passengers']:
        random_id = insert_passenger(client, passenger)
        random_ids.append(random_id)
    data['passengers'] = random_ids

    insert_fare_infos(client, data['fares'])
   
    for flight in data['flights']:
        insert_flight(client, flight)        



if (__name__ == '__main__'):
    main(sys.argv[1:])

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

    print 'Inserting flight %s' % flight['id']
    insert_airport_for_flight(client, flight)
    flights.new(flight['id'], data=flight).store()

def insert_passenger(client, passenger):
    name_array = passenger.keys()[0].split(' ')
    name, surname = name_array[-1], ' '.join(name_array[0:-1])
    key = uuid.uuid1().hex

    passengers = client.bucket(conf.buckets['passengers'])

    print 'Inserting passenger "%s,%s" with random key %s' % (name, surname, key)
    passengers.new(key, {'PassengerID': key, 'Surename': surname, 'name': name}).store()

def main(args=[]):
    print('Starting...')
    data = get_data(args)
    client = riak.RiakClient(host=conf.host, port=conf.port)


    random_ids = [] # TODO pythonize
    for passenger in data['passengers']:
        random_id = insert_passenger(client, passenger)
        random_ids.append(random_id)

    for flight in data['flights']:
        insert_flight(client, flight)        



if (__name__ == '__main__'):
    main(sys.argv[1:])

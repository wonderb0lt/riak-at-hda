#!/usr/bin/python2

''' Generates random data for insert.py '''

import random
import time
import json

def generate_entry():
	''' Generates a single entry. Returns a tuple: (id, data)'''

	_id = generate_id()
	flights = random_flights()
	personalflightdata = {}
	passengers = random_passengers(num=random.randint(1, 5))
	fare = random_fare_for(passengers, flights)

	for flight in flights:
		personalflightdata[flight['id']] = random_personal_for(flight)

	return (_id, {
		"id": _id,
		"personalflightdata": personalflightdata,
		"passengers": passengers,
		"flights": flights,
		"fares": fare
	})


# Some generators
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '1234567890'

def generate_id(length=6):
	return ''.join(random.sample(letters + digits, length))


def random_flights(count=2):
	return [random_flight() for i in xrange(count)]

def random_personal_for(flight):
	return {
		'class': random.choice(['Economy', 'Business']),
		'baggage': 'ADT %dPC' % random.randint(1, 3)
		# TODO: eTickets
	}

def random_fare_for(passengers, flights):
	name = random.choice(passengers)['id']
	base = len(flights) * 400 + random.randint(0, 100)
	tax = random.uniform(.04, .21)
	taxes = float(base) * tax
	total = round(base + tax, 2)
	curr = random.choice(['EUR', 'USD'])
	return {
			"segment": "*",
			"name": name,
			"type": "ADT",
			"fop": "Invoice",
			"base": base,
			"taxes": taxes, 
			"total": total,
			"currency": curr
	}

names = ['Stegmann', 'Becker', 'Bahro', 'Schreeck', 'Wolf', 'Weber', 'Lovecraft', 'Schaaf']
surnames = ['Patrick', 'Jens', 'Sven', 'Marcel', 'Sandra', 'H.P.', 'Sarah']

def random_passengers(num = 1):
	return [random_passenger() for i in xrange(num)]

def random_passenger():
	name = random.choice(names)
	surname = random.choice(surnames)
	_type = random.randint(0, 2)
	_id = '%s/%s' % (name.upper(), surname.upper())
	if _type == 1:
		_id += 'CHD'
	elif _type == 2:
		_id += 'INF'

	return {
				"id": _id, 
				"type": _type,
				"name": name,
				"surname": surname
	}

# Flight generation - much data to sample
airlines = ['Aeroflot', 'Air France', 'German Wings', 'Air Berlin', 'Lufthansa', 'Aer Lingus',
			'US Airways', 'Delta Airlines']
aircrafts = ['Airbus A380', 'Boeing 747', 'Airbus A320-200']
destinations = [
	{
		"country": "France",
		"city": "Paris",
		"iata":"ORY",
		"airport": "Orly Arpt",
		"terminals": ["W"]
	},
	{
		"country": "France",
		"city": "Montpellier",
		"iata":"MPL",
		"airport": "Frejorgues Arpt",
		"terminals": []
	},
	{
		"country": "Germany",
		"city": "Munich",
		"iata":"MUC",
		"airport": "Munich Intl Arpt",
		"terminal": "2"
	},
	{
			
		"country": "Germany",
		"city": "Dusseldorf",
		"iata":"DUS",
		"airport": "Dusseldorf Arpt",
		"terminal": ""
	},
	{
		"country": "France",
		"city": "Toulouse",
		"iata":"TLS",
		"airport": "Blagnac Arpt",
		"terminal": ""
	},
	{
		"country": "Thailand",
		"city": "Bangkok",
		"iata":"BKK",
		"airport": "Suvarnabhumi Intl Arpt",
		"terminal": ""
	}
]

def random_flight():
	_id = ''.join(random.sample(letters, 2)) + ''.join(random.sample(digits, 4))
	t = int(time.time())
	departure, arrival = (t, random.randrange(t, t+50000))
	duration = arrival-departure
	airline = random.choice(airlines)
	_from = random.choice(destinations)
	_to = random.choice(destinations)

	# Assert that from != to
	while _from == _to:
		_to = random.choice(destinations)

	# In rare cases, add a stop.
	if random.random() < .1:
		stops = random.choice(destinations)
	else:
		stops = []

	aircraft = random.choice(aircrafts)
	return {
			"id": _id,
			"departure": departure,
			"arrival": arrival,
			"duration": duration,
			"airline": airline,

			"from": _from,
			"to": _to,
			"stops": stops,
			"status": "Confirmed",
			"aircraft": aircraft
	}

if __name__ == '__main__':
	print 'For testing purposes, have this generated entry'
	print '*' * 20
	print json.dumps(generate_entry()[1])
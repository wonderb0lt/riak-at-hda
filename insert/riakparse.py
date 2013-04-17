#!/usr/bin/python
import itertools
import re
def parse(s):
	lines = s.split('\r\n')
	return {
		'id': split_and_strip(lines, 0),
		'passengers': parse_passengers(lines),
		'flights': list(parse_flights(lines))
	}

def split_and_strip(lines, idx):
	return lines[idx].split(':')[1].strip()

def parse_passengers(lines):
	passengers = []
	for line in lines[3:]:
		if line[0:6] == 'FLIGHT':
			break
		passengers.append([{name: _passenger_type(name)} for name in line.split(' ') if len(name) > 0]) # Pretty verbose!

	return list(itertools.chain(*passengers))

def _passenger_type(name):
	if name[-3:] == 'CHD':
		return 1
	elif name[-3:] == 'INF':
		return 2
	else:
		return 0

def regex(line, regex, no=0):
	return re.findall(regex, line)[no]

def parse_flights(lines):
	flight_starts = [idx for idx, line in enumerate(lines) if line[:6] == 'FLIGHT']

	for flight_section_start in flight_starts:
		yield {
			'id': regex(lines[flight_section_start], r'^FLIGHT:.+ \((.+)\) .+$'),
			'vendor_locator': regex(lines[flight_section_start], r'Vendor Locator: (.+)')
		}
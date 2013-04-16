#!/usr/bin/python
import itertools

def parse(s):
	lines = s.split('\r\n')
	return {
		'id': split_and_strip(lines, 0),
		'passengers': parse_passengers(lines),
		'flights': []
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
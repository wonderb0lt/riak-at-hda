#!/usr/bin/env python2

"""
Usage:
   delete.py  [--host=<host>] [--port=<port>] [--protocol=<prot>]

Options:
    --generate <number_of_entries>	Generate test data
    --host <host>					Target host [Default: localhost]
    --port <port>					Target port [Default: 8098]
    --protocol <prot>				Protocol to use [Default: pcb]

Examples:
    Insert a few files into a bucket (see conf.py):
        python insert.py data/006MME.json data/009GH1.json
    
    Generate test data (the amount is set in conf.py also):
        python insert.py --generate
"""


import sys
import json
import riak
import generate
from docopt import docopt
import uuid
import conf
import stopwatch
    

def main(args):
    if args['<file>']:
        data = get_data_from_file(args['<file>'])
        total = len(data)
    else:
        total = int(args['--generate'])
        data = generate_data(total)
#        total = conf.generation['number_of_entries']

    print 'Connecting to Riak...'
    host = args['--host']
    port = args['--port']
    prot = args['--protocol']

    if prot == 'http':
        client = riak.RiakClient(host=host, port=port)
    else:
        client = riak.RiakClient(host=host,  pb_port=port, protocol='pbc')

    bucket = client.bucket(conf.buckets['flights'])

    insert_timer = stopwatch.Timer()

    # New

	client.solr().delete('flights')
      

      
       print 'I\'m done.'


if __name__ == '__main__':
    main(docopt(__doc__))

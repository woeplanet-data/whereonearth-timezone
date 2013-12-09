#!/usr/bin/env python

# Experimental still... (20131209/straup)

import sys
import logging
import os
import os.path
import csv
import json
import pprint

def crawl(p):

    for root, dirs, files in os.walk(p):

        if len(dirs) == 0:
            
            for f in files:
                path = os.path.join(root, f)
                path = os.path.realpath(path)
                yield path

        else:
            for d in dirs:
                path = os.path.join(root, d)
                crawl(path)

def export(path, writer):

    fh = open(path, 'r')
    data = json.load(fh)

    f = data['features'][0]
    props = f['properties']

    # TO DO: trim decimal points and simplify

    geom = f['geometry']

    out = {
        'woeid': props['woe:id'],
        'tzid': props['fullname'],
        'geom': json.dumps(geom)
        }

    writer.writerow(out)

if __name__ == '__main__':

    import optparse

    parser = optparse.OptionParser()
    parser.add_option('-o', '--output', dest='output', action='store', default=None, help='write data to this source, default is STDOUT')
    parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='be chatty (default is false)')
        
    options, args = parser.parse_args()

    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    whoami = os.path.realpath(sys.argv[0])
    bin = os.path.dirname(whoami)
    root = os.path.dirname(bin)

    data = os.path.join(root, 'data')

    if options.output:
        fh = open(options.output, 'w')
    else:
        fh = sys.stdout

    fields = ('woeid', 'tzid', 'geom')

    writer = csv.DictWriter(fh, fields)
    writer.writeheader()

    for path in crawl(data):

        if not path.endswith('.geojson'):
            continue

        export(path, writer)

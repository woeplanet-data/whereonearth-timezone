#!/usr/bin/env python

# Still-experimental tool for flattening all the meta files in to a single .CSV
# file. Unclear what the relationship between this and meta/timezones.csv is
# (20131208/straup)

import sys
import logging
import os
import os.path
import csv

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

def flatten(path, writer):

    fh = open(path, 'r')
    reader = csv.DictReader(fh, delimiter='\t')

    for row in reader:

        out = {
            'swlat': row.get('bottom', None),
            'swlon': row.get('left', None),
            'nelat': row.get('top', None),
            'nelon': row.get('right', None),
            'name': row.get('name', ''),
            'woeid': row.get('woeid', 0),
            'offset': row.get('offset', None)
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

    meta = os.path.join(root, 'meta')

    if options.output:
        fh = open(options.output, 'w')
    else:
        fh = sys.stdout

    fields = ('swlat', 'swlon', 'nelat', 'nelon', 'name', 'woeid', 'offset')

    writer = csv.DictWriter(fh, fields)
    writer.writeheader()

    for path in crawl(meta):

        if os.path.basename(path) == 'timezones.csv':
            continue

        flatten(path, writer)

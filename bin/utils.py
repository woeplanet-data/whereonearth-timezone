import json
import re
import StringIO

def geometry2carbonite(geom):

    io = StringIO.StringIO()
    write_json(geom, io)

    io.seek(0)
    return io.read()

def write_json(data, out, indent=2): 

    # From TileStache's vectiles GeoJSON encoder thingy
    # (20130317/straup)

    float_pat = re.compile(r'^-?\d+\.\d+(e-?\d+)?$')
    charfloat_pat = re.compile(r'^[\[,\,]-?\d+\.\d+(e-?\d+)?$')

    encoder = json.JSONEncoder(separators=(',', ':'))
    encoded = encoder.iterencode(data)
    
    for token in encoded:
        if charfloat_pat.match(token):
            # in python 2.7, we see a character followed by a float literal
            out.write(token[0] + '%.6f' % float(token[1:]))
        
        elif float_pat.match(token):
            # in python 2.6, we see a simple float literal
            out.write('%.6f' % float(token))
        
        else:
            out.write(token)

def woeid2path(id):

    tmp = str(id)
    parts = []

    while len(tmp) > 3:
        parts.append(tmp[0:3])
        tmp = tmp[3:]

    if len(tmp):
        parts.append(tmp)

    return "/".join(parts)

def scrub_placetype(type):
    type = type.lower()
    type = type.replace(" ", "-")
    return type



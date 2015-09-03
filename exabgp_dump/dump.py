#!/usr/bin/python

from datetime import datetime
import json
import os
import pprint
import struct
from sys import stdin, stdout, stderr
import time


def ext_community_to_raw(value):
    raw = ''
    while value:
        b = struct.pack("B", value & 0xff)
        raw = b + raw
        value >>= 8

    if len(raw) < 8:
        raw = '\0' + raw

    return raw


while True:
    try:
        line = stdin.readline().strip()
        msg = json.loads(line)

        try:
            attribute = msg['neighbor']['message']['update']['attribute']
            ext_communities = attribute['extended-community']

            for idx in range(len(ext_communities)):
                ext_community = ext_communities[idx]
                raw = ext_community_to_raw(ext_community)
                if ord(raw[0]) == 0x00 and ord(raw[1]) == 0x02:
                    asn, number = struct.unpack('!HL', raw[2:8])
                    ext_communities[idx] = "target:%d:%d" % (asn, number)
        except:
            pass

        timestamp = datetime.fromtimestamp(msg['time'])
        stderr.write("# %s\n" % timestamp)
        stderr.write(pprint.pformat(msg, width=80) + "\n\n")
    except IOError:
        pass

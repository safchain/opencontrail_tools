#!/usr/bin/python

from sys import stdin, stdout, stderr
import time


ROUTE = '0.0.0.0/0'
NEXTHOP = '10.43.91.13'
ROUTE_TARGET = 'target:64512:555'
LABEL = 1000

msg = ('announce route %s next-hop %s local-preference 65000 '
       'rd %s:1 extended-community %s label %d')
msg = msg % (ROUTE, NEXTHOP, NEXTHOP, ROUTE_TARGET, LABEL)

stdout.write( msg + '\n')
stdout.flush()

while True:
    time.sleep(1)

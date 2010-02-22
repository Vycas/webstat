#!/usr/bin/env python

import sys
import hashlib
from urllib import urlopen
from datetime import datetime

url = sys.argv[1]
start = datetime.now()
try:
    site = urlopen(url)
except IOError:
    print 'Unable to open given url.'
    quit()
end = datetime.now()
time = end - start
body = site.read()
size = len(body)
speed = size * 1000.0 / time.microseconds
lines = body.count('\n') + 1
hash = hashlib.sha1(body)

print 'Speed: %.2f KB/s' % speed
print 'SHA-1:', hash.hexdigest()
print 'Size:', size
print 'Lines:', lines

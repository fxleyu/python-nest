# 3.2
from os.path import isfile, isdir

print isdir(r'/data/webroot/resource/python')
print isfile(r'/data/webroot/resource/python/test.txt')

# 3.3
try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python':2.7})

# 3.4
from __future__ import unicode_literals
s = 'am I an unicode?'
print isinstance(s, unicode)
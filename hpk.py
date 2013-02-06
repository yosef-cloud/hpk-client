#!/usr/bin/python

import re
import urllib

pgp_re = re.compile(r'''-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: ([^\n]+)

(.*)
-----END PGP PUBLIC KEY BLOCK-----''', re.S | re.M)
url = r'http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x%s'

def read_key(key_id):
    s = urllib.urlopen(url % key_id).read()
    match_obj = pgp_re.search(s)
    if not match_obj:
        return None
    contents = match_obj.group()
    return contents



print read_key('E75C6EF1C0FF7F41')


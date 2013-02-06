#!/usr/bin/python

import re
import urllib


class KeyServerBase(object):
    pass


class HKPServer(KeyServerBase):
    def __init__(self, server=None):
        super(HKPServer, self).__init__()
        self.server = server or 'http://pgp.mit.edu:11371'
        self.server = self.server.rstrip('/')

    def find(self, key_id):
        pgp_re = re.compile('(-----BEGIN PGP PUBLIC KEY BLOCK-----'
                            '.*-----END PGP PUBLIC KEY BLOCK-----)',
                            re.S | re.M)

        # key_id is received over the network, treat it as
        # unsafe user input and quote it.
        urlsane_key_id = urllib.quote(key_id)
        url = self.server + '/pks/lookup?op=get&search=' + urlsane_key_id

        s = urllib.urlopen(url).read()
        match_obj = pgp_re.search(s)
        if not match_obj:
            return None
        contents = match_obj.group()
        return contents

if __name__ == "__main__":
    keyserver = HKPServer()
    print keyserver.find('0xE75C6EF1C0FF7F41')

    keyserver2 = HKPServer(server='http://pool.sks-keyservers.net:11371/')
    print keyserver2.find('0xffb4080e2d5ae5f1')

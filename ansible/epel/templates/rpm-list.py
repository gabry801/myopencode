#!/usr/bin/python

import rpm

ts = rpm.TransactionSet()
mi = ts.dbMatch()
for h in mi:
    print "%s-%s-%s" % (h['name'], h['version'], h['release'])

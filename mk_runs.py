#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2018-S1-MU-67"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['M83'] = [ 91137, 91141, 91145, 91149, 91153,
              91262, 91266, 91270, 91542, 91565,
              91567, 91603, 91605, 91607, 91709,
              92335, 92341, 92815, 92817,
             ]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['M83']   = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['M83']   = "srdp=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)

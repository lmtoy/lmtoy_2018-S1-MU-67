#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2018-S1-MU-67"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['M83_CO']  = [ 91137, 91603 ]

on['M83_109'] = [ 91542, 91565, 91567, 91709]

on['M83_88']  = [ 91141, 91145, 91149, 91153,-91262,
                 -91266,-91270, 91605, 91607, 92335,
                  92341, 92815, 92817]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['M83_CO']   = "dv=150 dw=250"
pars1['M83_109']  = "dv=150 dw=250"
pars1['M83_88']   = "dv=150 dw=250"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['M83_CO']   = "srdp=1 admit=0"
pars2['M83_109']  = "srdp=1 admit=0"
pars2['M83_88']   = "srdp=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)

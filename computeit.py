#!/usr/bin/env python
import sys
import compute
from compute import compute as comp

myfile = sys.argv[1]
resultfile = sys.argv[2]

infile = open(myfile, 'r')
outfile = open(resultfile,'w')

for line in infile:
        answer = comp(line)
        outfile.write(str(answer)+'\n')

print 'Your answers have been written to %s'%(sys.argv[2])

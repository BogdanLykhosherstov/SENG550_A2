#!/usr/bin/env python
#mapperA2_1.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    row,column,value = line.split(',')
    inverted = [column,row]
    print('%s\t%s' %(inverted,value))

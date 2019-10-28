#!/usr/bin/env python
#reducerA2_1.py

import string
import sys
import re

for line in sys.stdin:
    # print(line)
    line = line.rstrip()
    transposed,value = line.split('\t')
    row,column = re.findall(r'\d+',transposed)
    print ('%s,%s,%s' %(row,column,value))
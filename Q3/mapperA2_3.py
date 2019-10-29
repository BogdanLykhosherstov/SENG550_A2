#!/usr/bin/env python
#mapperA2_3.py

import string
import sys
import re

for line in sys.stdin:
  
    line = line.strip()
    
    words = line.split(" ")
    for word in words:
        for nextWord in words:
            if(word!=nextWord):
                print ('%s %s'%(word,nextWord))


    
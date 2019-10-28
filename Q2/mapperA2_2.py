#!/usr/bin/env python
#mapperA2_2.py

import string
import sys
import re

for line in sys.stdin:
  
    line = line.strip()
    nodeInfo =line.split(' ')[-1]
    nodeId = line.split(' ')[0]
   
    adjList,distance,color,parentNode = nodeInfo.split('|')

    # if w or b, emit as is
    if color == "BLACK" or color == "WHITE":
        print('%s\t%s' %(nodeId,nodeInfo))
    elif color == "GRAY":
        nodeInfo = adjList+'|'+distance+'|'+"BLACK"+'|'+parentNode
        print('%s\t%s' %(nodeId,nodeInfo))
        # for each kid node:
        kidList = adjList.split(',')
        for kid in kidList:
            nodeInfo = 'null'+'|'+str(int(distance)+1)+'|'+"GRAY"+'|'+nodeId
            print('%s\t%s' %(kid,nodeInfo))
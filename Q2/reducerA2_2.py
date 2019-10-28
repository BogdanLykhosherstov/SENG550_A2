#!/usr/bin/env python
#reducerA2_2.py

import string
import sys
import re

nodeMap = {}

for line in sys.stdin:
  
    line = line.strip()
    nodeInfo =line.split('\t')[-1]
    nodeId = line.split('\t')[0]
   
    adjList,distance,color,parentNode = nodeInfo.split('|')
    

    # if adding for the first time
    if nodeId not in nodeMap:
        nodeMap[nodeId]=[adjList,distance,color,parentNode]
    # if already exists
    else:
        # skip visited nodes of color BLACK
        if(nodeMap[nodeId][2]=="BLACK"):
            continue
        # if initial node with kids adjList, populate adjList in dictionary
        if(adjList!="null"):
            nodeDetails = nodeMap[nodeId]
            nodeDetails[0]=adjList
            nodeMap[nodeId]=nodeDetails
        # else, processed node, with null adj list
        else:
            nodeDetails = nodeMap[nodeId]
            # smallest distance is kept
            if(distance<nodeDetails[1]):
                nodeDetails[1]=distance
            nodeDetails[3]=parentNode
            if(color=="BLACK"):
                nodeDetails[2]=color
            elif(color=="GRAY"):
                if(nodeDetails[2]=="WHITE"):
                    nodeDetails[2]=color
            nodeMap[nodeId]=nodeDetails
# print contents of map
for key in nodeMap:
    print('%s\t%s'%(key,nodeMap[key][0]+'|'+nodeMap[key][1]+'|'+nodeMap[key][2]+'|'+nodeMap[key][3]))

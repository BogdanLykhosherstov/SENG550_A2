#!/usr/bin/env python
#reducerA2_3.py

from fractions import Fraction as frac
import string
import sys
import re

# array of [key,value,countTogether]
# doesnt reset on change of key
listOfWords = []
elementWithAnything = {}

prevValue = ""
prevKey = ""
# keep track of pair count, reset on change of key
pairCount=0

for line in sys.stdin:
    
    line = line.strip()
    key,value = line.split(" ")
    # first run
    if(prevKey=="" and prevValue==""):
        prevKey=key
        prevValue=value
        pairCount+=1
    
    # --- Cases:

    # 1. same key, different value
    elif(key==prevKey and value!=prevValue):
        
        listOfWords.append([prevKey,prevValue,pairCount])
        
        prevValue = value
        # reset pairCount for another pair
        pairCount=1

    # 2. same key, same value
    elif(key==prevKey and value==prevValue):
        pairCount+=1
 
    # 3. different key
    elif(key!=prevKey):
        listOfWords.append([prevKey,prevValue,pairCount])
        prevValue = value
        prevKey = key

        pairCount=1

listOfWords.append([prevKey,prevValue,pairCount])

# print elements of listOfWords (numerators)
for element in listOfWords:
    if(element[0] not in elementWithAnything):
        elementWithAnything[element[0]]=1
    else:
        elementWithAnything[element[0]]+=element[2]
    
    # print(""+element[0]+","+element[1]+": "+str(element[2]))

# populate denominator for each key

# print("Element w/ Anything Count: ")
# for element in elementWithAnything:
    # print("N "+str(element)+" = "+str(elementWithAnything[element]))

for element in listOfWords:
    print(element[0],element[1],frac(int(element[2]),int(elementWithAnything[element[0]])))




   
    

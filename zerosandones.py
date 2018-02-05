# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:27:40 2018

@author: adi44
"""
import sys,numpy
if sys.version_info[0]>=3: raw_input=input
a=[int(e) for e in raw_input().split()]
print(numpy.zeros(a, dtype = numpy.int))
print(numpy.ones(a, dtype = numpy.int))



import sys,numpy
if sys.version_info[0]>=3: raw_input=input
n,m,p=map(int,raw_input().split())
for iter in range(0,(2*p)):
    if iter < p:
        print(numpy.zeros((n,m), dtype = numpy.int))
        if(iter < p-1):
         #   print("\n")
    else:
        print(numpy.ones((n,m), dtype = numpy.int))
        print("\n")
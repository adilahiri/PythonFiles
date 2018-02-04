# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:09:30 2018

@author: adi44
"""
import sys,numpy
if sys.version_info[0]>=3: raw_input=input
n,m=map(int,raw_input().split())
a=[]
for _ in range(n):
	a.append([int(e) for e in raw_input().split()])
a=numpy.array(a)
sum_array=numpy.sum(a, axis = 0)
prod=numpy.prod(sum_array)
print(prod)
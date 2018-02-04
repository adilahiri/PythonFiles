# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:20:51 2018

@author: adi44
"""
import sys,numpy
if sys.version_info[0]>=3: raw_input=input
n,m,p=map(int,raw_input().split())
a=[]
for _ in range(n+m):
	a.append([int(e) for e in raw_input().split()])
a=numpy.array(a)
b=a[0:n,:]
c=a[n:n+m,:]
print(numpy.concatenate((b,c), axis = 0))

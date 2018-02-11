# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:45:38 2018

@author: adi44
"""
import sys

def diagonalDifference(a):
    length= len(a)
    sum1=0
    sum2=0
    for iter in range(0,length):
        sum1= a[iter][iter] +sum1
        sum2 = sum2 + a[iter][len(a) -1-iter]
    
    diff= abs(sum2-sum1)
    return (diff)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
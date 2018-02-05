# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:41:28 2018

@author: adi44
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar=[]
    p=0
    for i in range (x+1):
        for j in range(y+1):
            for k in range (z+1):
                if i+j+K !=n :
                    ar.append([])
                    ar[p]=[i,j,k]
                    p=p+1
    print(ar)
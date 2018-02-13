# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:31:02 2018

@author: adi44
"""

def nearest_sq(n):
    iter = 0
    condition = True
    while (condition):
        if(((n+iter)**0.5).is_integer()):
            condition =False
            result=n +iter
        elif(((n-iter)**0.5).is_integer()):
            condition =False
            result = n -iter
        iter = iter +1
    return result 

a =nearest_sq(23)
    
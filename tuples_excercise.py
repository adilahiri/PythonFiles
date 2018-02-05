# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:38:22 2018

@author: adi44
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print (hash(t))
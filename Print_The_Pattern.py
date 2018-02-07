# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 00:30:13 2018

@author: adi44
"""
# print the pattern using just one print statement
# custom input example = 5
# 1
# 22
# 333
# 4444
# 55555
for i in range(1,int(input())): # than 2 lines will result in 0 score. Do not leave a blank line also
    print ((i*((10**(i-1)))) +  i*((10**(i-1))//9)  )
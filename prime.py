# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 17:43:26 2018

@author: Nanda Christanto
"""

"""bilangan prima antara 1-101""" 
def prime(x) :
    prim = True 
    if x >= 2 : 
        for i in range (2,x) :
            if x % i == 0 : 
                prim = False 
    else : 
        prim = False
    return prim

for i in range(1,101) :
    if prime(i) :
        print (i)
        
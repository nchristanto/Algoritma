# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 17:47:14 2018

@author: Nanda Christanto 
"""

"""bilangan fibbonacci"""
a,b,c = 0,1,0
for i in range(10) :
    print(a)
    c = a+b
    a = b
    b = c
    
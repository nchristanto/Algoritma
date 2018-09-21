# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:49:57 2018

@author: Nanda Christanto
"""
input = 1345679
digit = list(str(input))
jlh = len(digit)
for i in range (jlh):
    jlh_nol = jlh - i 
    number = digit[i].ljust(jlh_nol,'0')
    print(number)

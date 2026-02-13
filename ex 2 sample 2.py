# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 16:22:42 2026

@author: Agce
"""

year = int(input("Enter year:"))
if (year%400==0) or (year%4==0and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")
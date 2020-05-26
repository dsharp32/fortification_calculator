#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:51:55 2019

@author: Dan Sharp

This is a program to calculate the volume in millilitres of fortifying spirit 
to add to wine to raise it to a desired final percentage of alcohol. 
"""

import fortify
        
v_1 = float(input('Enter the initial volume to be fortified in millilitres:'))

p_1 = float(input('Enter the abv percentage of the inital volume:'))

p_2 = float(input('Enter the abv percentage of the fortifying spirit:'))

p_f = float(input('Enter the desired abv percentage of the final liquid:'))

v_x = fortify.return_v_x(v_1, p_1, p_2, p_f)

fortify.test_v_x(v_1, p_1, p_2, v_x, p_f)  

"""
Sample run:
fortification_calculator.py
Enter the initial volume to be fortified in millilitres:750

Enter the abv percentage of the inital volume:12.5

Enter the abv pecentage of the fortifying spirit:73.2

Enter the desired abv percentage of the final liquid:16.5
For a final abv of 16.5 percent add 53 millilitres of the fortifying spirit 
for a total volume of 803 millilitres.
"""
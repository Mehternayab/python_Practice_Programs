# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:46:16 2024

@author: DELL
"""

for i in range(1,101):
    if(i%5==0 and i%3==0):
        print(str(i)+" FuzzBuzz")
    elif(i%3==0):
        print(str(i)+" Fizz")
    elif(i%5==0):
        print(str(i)+" Buzz")
    
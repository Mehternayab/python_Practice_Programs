# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:21:35 2024

@author: DELL

"""

str = input("Enter the string")
key = input("Enter the key")



def find_the_str(str, key):
    
    arr = str.split()
    for i in arr:
        if(i==key):
            return i
        
        
print(find_the_str(str,key))


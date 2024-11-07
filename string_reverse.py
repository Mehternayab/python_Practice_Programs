# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:51:40 2024

@author: DELL
"""

def reverse_string(input_str):
    re_string=''
    for char in input_str:
        re_string=char+re_string
    return re_string
    
string = "Hello World!"
print(string) 
print(reverse_string(string))
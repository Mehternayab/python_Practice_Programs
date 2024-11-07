# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:59:47 2024

@author: DELL
"""


def replacechar(str1,char1):    
    result = ''
    for i in str1:
        #print (i)
        if i==' ':
            #print (i)
            i = char1
            result = result+i
        else :
            result += i
    return result
            
str1 = input('what is the string')
char1 = input('what is the char')
print(replacechar(str1, char1))
    
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:02:50 2024

@author: DELL
"""

#Check if string is Palindrome

def check_palindrome(input_string):
    check_string = ''.join(input_string.split()).lower()
    if check_string == check_string[::-1]:
        return True
    else:
        return False
    
    
    
input_string = "A man a plan a canal Panama" 
print("The give string is a palindrome: "+ str(check_palindrome(input_string)))
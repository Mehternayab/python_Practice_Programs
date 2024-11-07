# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:27:39 2024

@author: DELL
"""

def find_the_missing_num(num_list):
    num_list.sort()
    start_num = num_list[0]
    end_num = num_list[len(num_list)-1]
    orderd_list = [*range(start_num,end_num+1)]
    print(orderd_list)
    print(list((set(orderd_list).difference(num_list))))    
    
    
find_the_missing_num([90,96,97])
    

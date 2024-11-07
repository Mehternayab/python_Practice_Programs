# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:04:53 2024

@author: DELL
"""

def mergesort(arr):
    if len(arr)<=1:
        return arr
    left_half = arr[:len(arr)//2]
    right_half = arr[len(arr)//2:]
    
    left = mergesort(left_half)
    right = mergesort(right_half)
    
    return merge(left,right)

def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    result = []
    
    while left_pointer < len(left) and right_pointer <len(right):
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

arr = [9,8,7,6,5,4,3,2,1]
print(mergesort(arr))
    
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:01:26 2024

@author: DELL
"""

class sstack:
    def __init__(self):
        self.sstack = []
        self.spointer = 0
        
    def push_value(self,dataval):
        self.sstack.insert(self.spointer, dataval)
        self.spointer =  self.spointer+1
    def pop_value(self):
        if self.spointer == 0:
            print("Stack is empty")
        else:
            self.spointer = self.spointer-1
    def print_stack(self):
        if self.spointer == 0:
            print("stsack is empty")
        else:
            for i in range(self.spointer):
                print(self.sstack[i])
                
                
s = sstack()
s.print_stack()
s.pop_value()
s.push_value(1)
s.push_value(2)
s.push_value(3)
s.pop_value()  
s.print_stack()
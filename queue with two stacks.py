# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:04:51 2024

@author: DELL
"""

class twostack_queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def is_empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
    
    def enqueue(self,dataval):
        if self.is_empty() or not self.stack_out:
            self.stack_in.append(dataval)
            print("data added")
        else:
            while len(self.stack_out) != 0:
                self.stack_in.append(self.stack_out.pop())
            self.stack_in.append(dataval)
            print("data added")
            
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            if not self.stack_out:
                while len(self.stack_in) != 0:
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()
            else:
                return self.stack_out.pop()
            
q = twostack_queue()
print("queie is empty"+str(q.is_empty()))
#print(q.dequeue())
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(1)
print(q.dequeue())
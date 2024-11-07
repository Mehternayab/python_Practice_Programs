# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 00:21:07 2024

@author: DELL
"""

class listqueue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue)==0
    
    def enqueue(self,dataval):
        self.queue.append(dataval)
        print("data added to queue")
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue an empty queue")
        else:
            return self.queue.pop(0)
          
    def peek(self):
        if self.is_empty():
            raise IndexError("dequeue an empty queue")
        else:
            return self.queue[0]
        
    def size(self):
        return len(self.queue)
    
q = listqueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue size:", q.size())  # Output: 3
print("Front element:", q.peek())  # Output: 1
print("Dequeue:", q.dequeue())  # Output: 1
print("Queue size after dequeue:", q.size()) 
        
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:48:18 2024

@author: DELL
"""

class node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None
class linkedlistl:
    def __init__(self):
        self.headval = None
    def insert_data_at_end(self,dataval):
        if self.headval == None:
            self.headval = node(dataval)
        else:
            current_node = self.headval
            while current_node.nextval != None:
                current_node = current_node.nextval
            current_node.nextval = node(dataval)
            
    def print_linklist(self):
        if self.headval== None:
            print("Linked list is empty")
        else:
            current_node = self.headval
            while current_node!= None:
                print(current_node.dataval)
                current_node = current_node.nextval
        
    def insert_data_at_start(self,dataval):
        if self.headval == None:
            self.headval = node(dataval)
        else:
            new_node = node(dataval)
            new_node.nextval = self.headval
            self.headval = new_node
                
    def insert_data_at_index(self,dataval,index):
        posetion = 0
        if posetion == index:
            self.insert_data_at_start(dataval)
        else:
            current_node = self.headval
            while posetion+1 != index:
                current_node = current_node.nextval
                posetion = posetion+1
            new_node = node(dataval)
            new_node.nextval = current_node.nextval
            current_node.nextval = new_node
            
    def delete_data(self,dataval):
        if dataval == self.headval.dataval:
            self.headval = self.headval.nextval
        else:
            try:
                current_node = self.headval
                while dataval != current_node.dataval:
                    privious_node = current_node
                    current_node = current_node.nextval
                privious_node.nextval = current_node.nextval
            except:
                print("data not found")
    def print_linklist_after_jump(self):
        if self.headval== None:
            print("Linked list is empty")
        else:
            current_node = self.headval
            next_node = current_node.nextval
            while current_node!= None:
                print(current_node.dataval)
                current_node = next_node.nextval
                if current_node:                
                    if current_node.nextval == None:
                        print(current_node.dataval)
                        break
                    else:
                        next_node = current_node.nextval
                 
ll = linkedlistl()
ll.print_linklist()
ll.insert_data_at_end("abc")
ll.insert_data_at_end("1223")
ll.insert_data_at_end("jnkm")
ll.insert_data_at_end("jnjnlkmnk")
ll.insert_data_at_start("hi")
ll.insert_data_at_index("insert data", 0)
ll.insert_data_at_end("hgvgvjygjh")
ll.insert_data_at_end("jijiji")
ll.print_linklist()
print()
ll.delete_data("insert data")
ll.print_linklist()
print()
ll.print_linklist_after_jump()
        
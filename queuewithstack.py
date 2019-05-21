# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:07:35 2018

@author: Administrator
"""
class stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.insert(0,data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size()==0
    
class queueusingstack:
    def __init__(self):
        self.s1=stack()
        self.s2=stack()
    def enqueue(self,data):
        self.s1.push(data)
        if not self.s1.isEmpty():
            while self.s1.size() > 0:
                self.s2.push(self.s1.pop())
        
    def dequeue(self):
        
        return self.s2.pop()
        
if __name__=='__main__' :       
 q=queueusingstack()
 q.enqueue(1)
 q.enqueue(2)
 a=q.dequeue()
 b=q.dequeue()
 print(a)
 print(b)
 
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:07:19 2019

@author: Lavi
"""

class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
 
    def is_empty(self):
        return self.queue2.is_empty()
 
    def push(self, data):
        self.queue1.enqueue(data)
        while not self.queue2.is_empty():
            x = self.queue2.dequeue()
            self.queue1.enqueue(x)
        self.queue1, self.queue2 = self.queue2, self.queue1
 
    def pop(self):
        return self.queue2.dequeue()
    
    
 
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
 
 
s = Stack()
 
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())


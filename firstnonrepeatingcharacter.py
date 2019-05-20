# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:32:11 2019

@author: Lavi

"""
from queue import Queue
def firstnonrepeat(s):
    q=Queue()
    global MAX_CHAR
    charcount=[0]*MAX_CHAR
    for i in range(len(s)):
        q.put(s[i])        
        charcount[ord(s[i])-ord('a')]+=1
        print(charcount)
        while (not  q.empty()): 
            if charcount[ord(q.queue[0])-ord('a')] >1:
                q.get()
            else:
                print(q.queue[0])
                break
        if(q.empty()):
            print(-1)
    print()
MAX_CHAR=26
s="aabc"
firstnonrepeat(s)
               
 
 

            
            
        
    
    
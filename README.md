# Stacks and Queues :
1.Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.
Examples:
a) For any array, rightmost element always has next greater element as -1.
b) For an array which is sorted in decreasing order, all elements have next greater element as -1.
c) For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.

Element       NGE

   4      -->   5

   5      -->   25

   2      -->   25

   25     -->   -1

d) For the input array [13, 7, 6, 12}, the next greater elements for each element are as follows.

  Element        NGE

   13      -->    -1

   7       -->     12

   6       -->     12

   12     -->     -1

2.Implement a Queue using 2 stackss1 and s2 .

3.Implement a Stack using 2 queueq1 and q2 .

4.Implement a Stack in which you can get min element in O(1) time and O(1) space.

5.The task is to design and implement methods of an LRU cache. The class has two methods get and set which are defined as follows.
get(x)   : Gets the value of the key x if the key exists in the cache otherwise returns -1
set(x,y) : inserts the value if the key x is not already present. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
In the constructor of the class the size of the cache should be initialized.

6.Given an input stream of n characters consisting only of small case alphabets the task is to find the first non repeating character each time a character is inserted to the stream. If no non repeating element is found print -1.

Example
Flow in stream : a, a, b, c

a goes to stream : 1st non repeating element a (a)

a goes to stream : no non repeating element -1 (a, a)

b goes to stream : 1st non repeating element is b (a, a, b)

c goes to stream : 1st non repeating element is b (a, a, b, c)

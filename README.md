# Binary-Heap-Tree-Python-implementation

A binary heap is a complete binary tree which satisfies the heap ordering property.

A Binary Heap is a Binary Tree with two properties:
1) It is a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap.
In a Min Binary Heap, the min-heap property: the value of each node is greater than or equal to the value of its parent, with the minimum-value element at the root. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to Min Heap.
 This repo is a python code that demostrates the implimentation of a binary haep tree
 
# Explanation of the code

Let me explain the code to you. First, a class is created with several member functions inside it. We will see them one by one.

 The first method we used is Length. The Length()  returns the number of elements in the heap.
 
 
 The second method is the left_child() which returns the index of the left child of the argument.
 
 
 The third method right_child() which returns the index of the right child of the argument.
 
 
The next method Parent() returns the index of the parent of the argument.


The Get_Index() method takes an index as an argument and returns the key at the index.


The get_max() method gives the maximum element in the heap.


The Extract_maximum() method removes the maximum element from the heap.


The method max_heapify() modifies the heap structure to satisfy the heap property.


The swap() method takes two indexes as arguments and exchanges the corresponding elements in the heap.

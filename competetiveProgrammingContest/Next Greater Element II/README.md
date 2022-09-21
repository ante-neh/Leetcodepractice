
Find the next greater element for every element in a circular array

Given a circular integer array, find the next greater element for every element in it. The next greater element of an element x in the array is the first larger number to the next of x.

In a circular array, the indices will wrap around as if it were connected end-to-end. In other words, the end of the array wraps around to the start of the array. Therefore, we can search circularly to find the next greater number. If the next greater element doesn’t exist, consider it to be -1.

 
For example,
Input:  [3, 5, 2, 4]
Output: [5, -1, 4, 5]
 
Input:  [7, 5, 3, 4]
Output: [-1, 7, 4, 7] 
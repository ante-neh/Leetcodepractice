Q7. Find k’th Node from End of Linked List


Problem Statement

Problem Description : 
Given a linked list LL and a positive integer k, find the kth node from the end of the list.

Note: If k is greater than the size of the list, return null.

Input: 
First Argument : head of the linked list LL
Second Argument : A positive integer k

Output: 
Kth Node from the end of the given list.

Example 1 :

Input : 
LL = 1 -> 2 -> 3 -> 4 -> 5
k = 2

Output: Node with data 3


Explanation : 
As per input, the 2nd node from the end of the linked list is 4.

Example 2 :

Input : 
LL = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
k = 13

Output: 
null

Explanation : 
Given Linked List has 10 nodes and we are trying to find the 13th node from the end of the list, which does not exist. So output is null.

Find floor and ceil of a number in a sorted integer array

Given a sorted integer array, find the floor and ceil of a given number in it. The floor and ceil map the given number to the largest previous or the smallest following integer in the array.

More precisely, for a number x, floor(x) is the largest integer in the array less than or equal to x, and ceil(x) is the smallest integer in the array greater than or equal to x. If the floor or ceil doesn’t exist, consider it to be -1. For example,

Example:

Input: nums = [1, 4, 6, 8, 9]
       target = 4

Output: [4,4]

Example 2:

Input: nums = [1,4,6,8,9]
       target = 7

Output:[6,8]

Input:nums = [1,4,6,8,9]
      target = 10

OutPut = [9,-1]

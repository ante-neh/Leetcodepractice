# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printNthFromLast(self,head, n):
        temp=head
        length=0
        while temp and temp.next:
            temp=temp.next
            length+=1
        for i in range(length-n):
            temp=temp.next
        return temp.val
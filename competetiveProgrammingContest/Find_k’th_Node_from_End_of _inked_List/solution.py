# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printNthFromLast(self,head, n):
        fast,slow=head,head
        for i in range(n):
            if fast!=None:
                fast=fast.next
            else:
                return None
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        return slow
        
        
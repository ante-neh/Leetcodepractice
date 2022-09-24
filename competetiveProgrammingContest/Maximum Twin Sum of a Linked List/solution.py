# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        temp,sum=head,0
        while temp:
            stack.append(temp.val)
            temp=temp.next
        n=len(stack)
        for i in range(n):
            sum=max(sum,(stack[i]+stack[n-i-1]))
        return sum
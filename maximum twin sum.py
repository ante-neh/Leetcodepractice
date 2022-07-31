# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=head
        stack=[]
        sum=0
        while temp:
            stack.append(temp.val)
            temp=temp.next
        length=len(stack)
        for i in range(length):
            sum=max(sum,(stack[i]+stack[length-i-1]))
        return sum
    #time complexity O(n)
    #space complexity O(n)
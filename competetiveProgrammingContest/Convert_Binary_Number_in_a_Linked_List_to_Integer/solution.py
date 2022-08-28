# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp=head
        stack=[]
        sum=0
        while temp and temp.next:
            stack.append(temp.val)
            temp=temp.next
        for i in range(len(stack)):
            sum+=stack.pop()*(2**i)
        return sum
        

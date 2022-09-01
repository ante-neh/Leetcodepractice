# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_rev,l2_rev=self.reverse(l1),self.reverse(l2)
        carry,current=0,None
        while l1_rev or l2_rev or carry:
            val1=l1_rev.val if l1_rev else 0
            val2=l2_rev.val if l2_rev else 0
            val=val1+val2+carry
            carry=val//10
            val=val%10
            node=ListNode(val)
            node.next=current
            current=node
            l1_rev=l1_rev.next if l1_rev else None
            l2_rev=l2_rev.next if l2_rev else None
        return current
    def reverse(self,head):
        prev,current=None,head
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        return prev
    #time complexity O(n)
    #space complexity O(n)
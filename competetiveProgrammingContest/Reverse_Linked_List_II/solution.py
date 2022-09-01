# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        current,prev=head,prev
        while left>1:
            prev=current
            current=current.next
            left-=1
        tail,con=prev,current
        while current and left<=right:
            next=current.next
            current.next=prev
            prev=current
            current=next
            left+=1
        tail.next=prev
        con.next=current
        return head
        
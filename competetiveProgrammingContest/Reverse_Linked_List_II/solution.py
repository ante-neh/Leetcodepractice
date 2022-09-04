# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        leftPrev,current=dummy,head
        for i in range(left-1):
            leftPrev=current
            current=current.next
        leftCon,rightCon=leftPrev,current
        prev=None
        while current and left<=right:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
            left+=1
        leftCon.next,rightCon.next=prev,current
        return dummy.next
        
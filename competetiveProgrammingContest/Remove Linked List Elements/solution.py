# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur=dummy=ListNode(0,head)
        temp=head
        while temp:
            if temp.val==val:
                cur.next=temp.next
            else:
                cur=cur.next
            temp=temp.next
        return dummy.next
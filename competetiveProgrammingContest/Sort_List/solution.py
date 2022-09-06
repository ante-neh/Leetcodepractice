# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left=head
        right=self.getMid(head)
        temp=right.next
        right.next=None
        right=temp
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
    def getMid(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
    def merge(self,list1,list2):
        head=dummy=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                head.next=list1
                list1=list1.next
            else:
                head.next=list2
                list2=list2.next
            head=head.next
        if list1:
            head.next=list1
        elif list2:
            head.next=list2
        return dummy.next
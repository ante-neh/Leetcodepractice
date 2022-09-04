# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = ListNode(0,head)
        groupPrev=node
        while True:
            kth=self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext=kth.next
            prev,current=kth.next,groupPrev
            while current!=groupNext:
                next=current.next
                current.next=prev
                prev=current
                current=next
            temp=groupPrev.next
            groupPrev.next=kth
            groupPrev=temp
        return node.next
    def getKth(self,current,k):
        while k>0:
            current=current.next
            k-=1
        return current
    
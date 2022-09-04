# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast,slow=head,head
        for i in range(k-1):
            fast=fast.next
        left=fast
        while fast.next:
            fast=fast.next
            slow=slow.next
        left.val,slow.val=slow.val,left.val
        return head
        #time complexiyt O(n)
        #space complexity O(1)
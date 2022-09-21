# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp=head
        linkedList=[]
        while temp:
            linkedList.append(temp.val)
            temp=temp.next
        stack=[]
        result=[0]*len(linkedList)
        for i,num in enumerate(linkedList):
            while stack and stack[-1][0]<num:
                val,index=stack.pop()
                result[index]=num
            stack.append([num,i])
        return result
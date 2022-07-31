# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer,stack=[],[]
        temp=head
        while temp:
            answer.append(temp.val)
            temp=temp.next
        result=answer[:]
        for i,n in enumerate(answer):
            while stack and answer[stack[-1]]<n:
                index=stack.pop()
                result[index]=n
            stack.append(i)
        for i in range(len(result)):
            if result[i]==answer[i]:
                result[i]=0
        return result
    #time  complexity O(n)
    #space complexity O(n)
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        for i in range(1,max(target)+1):
            stack.append('Push')
            if i not in target:
                stack.append('Pop')
        return stack
class Solution:
    def maxDepth(self, s: str) -> int:
        counter=0
        depth=float("-inf")
        for char in s:
            if char=='(':
                counter+=1
            elif char==')':
                counter-=1
            depth=max(depth,counter)
        return depth
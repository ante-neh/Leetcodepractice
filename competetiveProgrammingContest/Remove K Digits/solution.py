class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for char in num:
            while stack and stack[-1]>char and k>0:
                stack.pop()
                k-=1
            stack.append(char)
        stack=stack[:len(stack)-k]
        return str(int(''.join(stack))) if stack else '0'
    
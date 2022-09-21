class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen={']':'[','}':'{',')':'('}
        stack=[]
        for braces in s:
            if braces in closeToOpen:
                if stack and stack[-1]==closeToOpen[braces]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(braces)
        return not stack
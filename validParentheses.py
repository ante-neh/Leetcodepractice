class Solution:
    def isValid(self, s: str) -> bool:
        braces = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for chr in s:
            if chr in braces.values():
                stack.append(chr)
            elif chr in braces:
                if stack and braces[chr] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack
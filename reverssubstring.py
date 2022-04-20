class Solution:
    def reverseParentheses(self, s: str) -> str:
            stack = []
            for ch in s:
                if ch == ')':
                    st = ''
                    while stack and stack[-1] != '(':
                        st += stack.pop()[::-1]

                    stack.pop()
                    stack.append(st)
                else:
                    stack.append(ch)

            return "".join(stack)
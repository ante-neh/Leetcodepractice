class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        idx = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[idx]:
                idx += 1
                stack.pop()
        return len(stack)==0
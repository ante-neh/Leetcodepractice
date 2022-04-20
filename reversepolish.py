class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                #print(stack)
                num2, num1 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(num1+num2)
                if token == "-":
                    stack.append(num1-num2)
                if token == "*":
                    stack.append(num1*num2)
                if token == "/":
                    stack.append(int(num1/num2))
            else:
                stack.append(int(token))
        return stack.pop()
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operater = ""
        num =""
        for i,c in enumerate(s):
            if '0' <= c <= '9':
                num += c
               
            if c == '+' or c == '*' or c == '-' or c == '/' or i == len(s) - 1:
                if operater == "":
                    stack.append(int(num))     
                if operater == '+': 
                    stack.append(int(num))        
                if operater == '*':
                    stack.append(stack.pop()*int(num))         
                if operater == '-':
                    stack.append(-1*int(num))
                if operater == '/':
                    stack.append(int(stack.pop()/int(num)))
                num = ""
                operater = c
             
        return sum(stack)
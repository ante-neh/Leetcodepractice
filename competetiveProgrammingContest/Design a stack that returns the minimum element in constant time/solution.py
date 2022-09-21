class MinStack:
    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self,val):
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif val<=self.minStack[-1]:
            self.minStack.append(val)
    def pop(self):
        if not self.stack:
            return 
        top=self.stack.pop()
        if top==self.minStack[-1]:
            self.minStack.pop()
        return top
    def top(self):
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)
    def size(self):
        return len(self.stack)
    def getMin(self):
        if not self.minStack:
            return 
        else:
            return self.minStack[-1]

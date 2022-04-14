class MyQueue:
   def __init__(self):
      self.stk1 = []
      self.stk2 = []


   def push(self, x: int) -> None:
      self.stk1.append(x)


   def pop(self) -> int:
      if self.stk2:
         return self.stk2.pop()
      while self.stk1:
         self.stk2.append(self.stk1.pop())
      return self.stk2.pop()


   def peek(self) -> int:
      return self.stk2[-1] if self.stk2 else self.stk1[0]

def empty(self) -> bool:
	   return not (self.stk1 or self.stk2)
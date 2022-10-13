class Solution:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack=[]
        for n in nestedList:
            self.flatten(n)
    def flatten(self,item):
        if item.isInteger():
            self.stack.append(item.getInteger())
        else:
            for i in item.getList():
                self.flatten(i)
    def next(self) -> int:
        return self.stack.pop()
    def hasNext(self) -> bool:
         return len(self.stack)
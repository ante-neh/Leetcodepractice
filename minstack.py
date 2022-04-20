class MinStack:

    def __init__(self):
        self.list = []
    def push(self, val: int) -> None:
        self.list.append(val)
        return None
    def pop(self) -> None:
        self.list.pop()
        return None
    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return min(self.list)
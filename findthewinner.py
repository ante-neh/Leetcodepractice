import collections
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = collections.deque([i for i in range(1, n+1)])
        counter = k - 1
        while len(q) > 1:
            while q and counter > 0 and len(q) > 1:
                q.append(q.popleft())
                counter -= 1
            q.popleft()
            counter = k - 1
            
        return q[0]
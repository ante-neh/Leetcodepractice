class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderIndex = {c:i for i, c in enumerate(order)}
        
        s = list(s)
        
        s.sort(key = lambda c:orderIndex.get(c,len(s)))
        
        return ''.join(s)
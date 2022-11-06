class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        
        def canBreak(x, y):
            for i in range(len(x)):
                if x[i] < y[i]:
                    return False
                
            return True
        
        return canBreak(s1,s2) or canBreak(s2,s1)
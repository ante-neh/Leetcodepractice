class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t=sorted(s),sorted(t)
        return s==t
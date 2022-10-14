class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        maxLen=1
        l=0
        for r in range(1,len(s)):
            if ord(s[r])-ord(s[r-1])==1:
                maxLen=max(maxLen,r-l+1)
                continue
            else:
                l=r
        return maxLen
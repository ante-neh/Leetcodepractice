class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        niceSubstring = ""
        for windowEnd in range(len(s)): 
            for windowStart in range(windowEnd+1): 
                substring = s[windowStart:windowEnd+1]
                if len(set(substring.lower())) == (len(set(substring)) // 2): 
                    niceSubstring = max(niceSubstring, substring, key=len)
        return niceSubstring
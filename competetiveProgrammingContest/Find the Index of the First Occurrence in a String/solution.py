class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, len(needle)
        
        while l + r < len(haystack) + 1:
            sub = haystack[l:l+r]
            if sub == needle:
                return l
            l += 1
            
        return -1
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        l,r=0,k
        while l<len(s) and r<len(s):
            s[l:r]=s[l:r][::-1]
            l+=2*k
            r+=2*k
        if l<len(s):
            s[l:]=s[l:][::-1]
        return ''.join(s)
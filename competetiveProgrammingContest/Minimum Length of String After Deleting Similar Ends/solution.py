class Solution:
    def minimumLength(self, s: str) -> int:
        s=list(s)
        l,r=0,len(s)-1
        while l<r:
            while l<r and s[l]==s[r]:
                l+=1
            while r>=l and l>0 and s[l-1]==s[r]:
                r-=1
            if s[l]!=s[r]:
                break
        if l>r:
            return 0
        return r-l+1
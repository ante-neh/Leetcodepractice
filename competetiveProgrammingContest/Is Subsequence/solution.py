class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,j=0,0
        outPut=''
        while l<len(s) and j<len(t):
            if s[l]==t[j]:
                outPut+=s[l]
                l+=1
                j+=1
            else:
                j+=1
        return s==outPut
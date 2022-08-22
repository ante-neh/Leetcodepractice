class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        sCount={}
        counter=0
        l=0
        for r in range(len(s)):
            sCount[s[r]]=1+sCount.get(s[r],0)
            if r-l+1==3:
                if len(sCount)==3:
                    counter+=1
                sCount[s[l]]-=1
                if sCount[s[l]]==0:
                    sCount.pop(s[l])
                l+=1
        return counter
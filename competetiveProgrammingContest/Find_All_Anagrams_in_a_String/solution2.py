class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount,pCount={},{}
        counter=0
        for char in p:
            pCount[ord(char)-ord('a')]=1
        l=0
        for r in range(len(s)):
            sCount[ord(s[r])-ord('a')]=1
            if (r-l+1)==len(p):
                if sCount==pCount:
                    counter+=1
                sCount[ord(s[l])-ord('a')]=0
                l+=1
        return counter

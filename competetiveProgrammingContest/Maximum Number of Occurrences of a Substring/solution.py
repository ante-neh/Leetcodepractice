class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        sCount={}
        counter=0
        for r in range(len(s)-minSize+1):
            sub=s[r:r+minSize]
            if minSize>=len(set(sub)) and len(set(sub))<=maxSize:
                sCount[sub]=1+sCount.get(sub,0)
                counter=max(sCount[sub],counter)
        return counter
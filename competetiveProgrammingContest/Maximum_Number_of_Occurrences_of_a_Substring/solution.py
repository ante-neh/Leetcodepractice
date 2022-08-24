class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        sCount={}
        counter=0
        for i in range(len(s)-minSize+1):
            sub=s[i:i+minSize]
            if len(set(sub))<=maxSize and len(set(sub))<=maxLetters:
                sCount[sub]=1+sCount.get(sub,0)
                counter=max(sCount[sub],counter)
        return counter
    #time complexity O(n)
    #space complexity O(n)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count,maxLen=0,float('-inf')
        l,vowels=0,['a','e','i','o','u']
        for r in range(len(s)):
            if s[r] in vowels:
                count+=1
            if r-l+1==k:
                maxLen=max(maxLen,count)
                if s[l] in vowels:
                    count-=1
                l+=1
        return maxLen
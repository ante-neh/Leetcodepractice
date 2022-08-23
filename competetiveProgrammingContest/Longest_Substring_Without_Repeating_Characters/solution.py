class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        counter=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            counter=max(counter,r-l+1)
        return counter
#time complexity O(n)
#space complexity O(1)
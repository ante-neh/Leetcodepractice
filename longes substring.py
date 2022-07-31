class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        left=0
        counter=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[r])
            counter=max(counter,r-left+1)
        return counter
    #time complexity O(n)
    #space complexity O(n)
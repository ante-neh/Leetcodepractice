class Solution:
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        l,maxLen=0,0
        sCount={}
        for r in range(len(s)):
            sCount[s[r]]=1+sCount.get(s[r],0)
            while len(sCount)>k:
              sCount[s[l]]-=1
              if sCount[s[l]]==0:
                sCount.pop(s[l])
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen

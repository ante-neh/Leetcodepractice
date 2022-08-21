def characterReplacement(self, s, k):
    sCount={}
    l=0
    maxLen=0
    for r in range(len(s)):
        sCount[s[r]]=1+sCount.get(s[r],0)
        while (r-l+1)-max(sCount.values())>k:
            sCount[s[l]]-=1
            l+=1
        maxLen=max(maxLen,r-l+1)
    return maxLen
#time complexity o(n)
#space complexity (n)

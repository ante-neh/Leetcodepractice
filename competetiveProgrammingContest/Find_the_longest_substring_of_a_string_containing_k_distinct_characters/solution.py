def getLongest(s, k):
    l=0
    sCount={}
    maxLen=0
    for r in range(len(s)):
        sCount[s[r]]=1+sCount.get(s[r],0)
        while len(sCount)>k:
            sCount[s[l]]-=1
            if sCount[s[l]]==0:
                sCount.pop(s[l])
            l+=1
        maxLen=max(maxLen,r-l+1)
    return maxLen
#time complexity O(n)
#space complexity O(1)
        
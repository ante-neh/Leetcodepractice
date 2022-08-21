class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count,s2Count={},{}
        for i in range(len(s1)):
            s1Count[s1[i]]=1+s1Count.get(s1[i],0)
        l=0
        for r in range(len(s2)):
            s2Count[s2[r]]=1+s2Count.get(s2[r],0)
            if (r-l+1)==len(s1):
                if s2Count==s1Count:
                    return True
                s2Count[s2[l]]-=1
                if s2Count[s2[l]]==0:
                    s2Count.pop(s2[l])
                l+=1      
        return False
    #time complexity O(n)
    #space complexity O(n)
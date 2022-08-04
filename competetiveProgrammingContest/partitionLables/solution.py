class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chach={}
        result=[]
        for i in range(len(s)):
            chach[s[i]]=i
        l=r=index=0
        while index<len(s):
            cur=s[index]
            r=max(r,chach[cur])
            if (r==index):
                size=r-l+1
                result.append(size)
                r+=1
                l=r
            index+=1
        return result
    
    #time complexity O(n)
    #space complexiyt O(n)
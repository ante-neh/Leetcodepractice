class Solution:
    def reorganizeString(self, s: str) -> str:
        s=list(s)
        countFreq={}
        for i in range(len(s)):
            countFreq[s[i]]=1+countFreq.get(s[i],0)
        countFreq=sorted(countFreq.items(),key=lambda item:item[1],reverse=True)
        indicies=list(range(0,len(s),2))+list(range(1,len(s),2))
        i=0
        for val,cnt in countFreq:
            while cnt>0:
                s[indicies[i]]=val
                cnt-=1
                i+=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                return ''
        return ''.join(s)
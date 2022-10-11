class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        countFreq={}
        for i in arr:
            countFreq[i]=1+countFreq.get(i,0)
        values=list(countFreq.values())
        values.sort(reverse=True)
        sum,counter=0,0
        length=len(arr)//2
        for i in range(len(values)):
            sum+=values[i]
            counter+=1
            if sum>=length:
                return counter
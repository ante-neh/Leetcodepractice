class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        countFreq={}
        for i in range(len(nums)):
            countFreq[nums[i]]=1+countFreq.get(nums[i],0)
        countFreq=sorted(countFreq.items(),key=lambda item:item[1])
        val,freq=None,0
        for i in range(len(countFreq)):
            if countFreq[i][0]%2==0 and countFreq[i][1]>freq:
                val,freq=countFreq[i][0],countFreq[i][1]
            elif countFreq[i][0]%2==0 and countFreq[i][1]==freq:
                val=min(val,countFreq[i][0])
        return val if val is not None else -1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countFreq={}
        for i in range(len(nums)):
            countFreq[nums[i]]=1+countFreq.get(nums[i],0)
        countFreq=sorted(countFreq.items(),key=lambda item:item[1])
        for i in range(len(countFreq)):
            if countFreq[i][1]>len(nums)//2:
                return countFreq[i][0]
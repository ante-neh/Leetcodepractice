class Solution:
    def countingSort(self,nums):
        result=[0]*len(nums)
        maxVal=max(nums)+1
        count=[0]*(maxVal)
        for i in range(len(nums)):
            count[nums[i]]+=1
        for i in range(1,len(count)):
            count[i]+=count[i-1]
        for i in range(len(nums)-1,-1,-1):
            result[count[nums[i]]-1]=nums[i]
            count[nums[i]]-=1
        return result
        
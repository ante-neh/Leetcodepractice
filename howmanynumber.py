class Solution:
    def smallerNumbersThanCurrent(self, nums):
        smaller=[0]*101
        k=max(nums)+1
        for i in range(len(nums)):
            smaller[nums[i]]+=1
        for i in range(1,k):
            smaller[i]=smaller[i]+smaller[i-1]
        for i in range(len(nums)):
            position=nums[i]
            if position==0:
                nums[i]=0
            else:
                nums[i]=smaller[position-1]
        return nums
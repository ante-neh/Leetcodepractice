class Solution:
    def targetIndices(self, nums, target: int):
        a=[]
        b=[]
        for i in range(len(nums)):
            min=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min]:
                    min=j                   
            if min!=i:
                nums[i],nums[min]=nums[min],nums[i]
            b.append(nums[i])
        for i in range(len(b)):
            if b[i]==target:
                a.append(i)
        return a
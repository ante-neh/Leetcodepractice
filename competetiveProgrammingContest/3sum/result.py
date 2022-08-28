class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i,num in enumerate(nums):
            if i>0 and nums[i-1]==num:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                threesum=num+nums[l]+nums[r]
                if threesum<0:
                    l+=1
                elif threesum>0:
                    r-=1
                else:
                    result.append([num,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return result
    #time complexity O(nlogn)
    #space complexity O(n)

def find3Numbers(nums,target):
    nums.sort()
    for i,num in enumerate(nums):
        l,r=i+1,len(nums)-1
        while l<r:
            sum=num+nums[l]+nums[r]
            if sum==target:
                return [num,nums[l],nums[r]]
            elif sum<target:
                l+=1
            else:
                r-=1
"""   
nums=[12, 3, 4, 1, 6, 9]
target=24
print(find3Numbers(nums, target))


#time complexity O(n**2)
#space complexity O(1)
"""
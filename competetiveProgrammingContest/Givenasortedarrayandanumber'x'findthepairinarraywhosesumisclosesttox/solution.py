def printClosest(nums,target):
    minDiff=10000 #the largest possible value in the array plus one you can get it in the constrant section of the problem statement
    l,r=0,len(nums)-1
    while l<r:
        sum=nums[l]+nums[r]
        if abs(sum-target)<minDiff:
            minDiff=abs(sum-target)
            indexR=r
            indexL=l
        if sum<=target:
            l+=1
        else:
            r-=1
    return [nums[indexL],nums[indexR]]
"""
nums=[1,3,4,7,10]
target=15
print(printClosest(nums,target))


time complexity O(n)
space complexity O(1)

"""
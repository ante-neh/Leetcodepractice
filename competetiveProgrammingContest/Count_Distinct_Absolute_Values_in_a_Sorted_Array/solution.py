def getCountDistinct(nums):
    counter=0
    numsCount={}
    for i in range(len(nums)):
        if nums[i]>=0 and nums[i] not in numsCount:
            numsCount[nums[i]]=1+numsCount.get(nums[i],0)
            counter+=1
    return counter
#time complexity O(n)
#space complexity O(n)

 
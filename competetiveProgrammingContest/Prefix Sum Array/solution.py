def prefix(nums):
    prefixSum=[]
    sum=0
    for i in range(0,len(nums)):
        sum+=nums[i]
        prefixSum.append(sum)
    return prefixSum

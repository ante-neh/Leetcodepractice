def prefix(nums):
    sum=0
    prefixSum=[]
    for i in range(len(nums)):
        sum+=nums[i]
        prefixSum.append(sum)
    return prefixSum
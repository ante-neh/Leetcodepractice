def getDuplicates(nums, k):
    numsCount={}
    for i in range(len(nums)):
        if i in numsCount and i-numsCount[nums[i]]<=k:
            return True
        else:
            numsCount[nums[i]]=i
    return False
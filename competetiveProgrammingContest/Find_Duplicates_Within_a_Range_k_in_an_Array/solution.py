def getDuplicates(nums, k):
    numsCount={}
    l=0
    for r in range(len(nums)):
        numsCount[nums[r]]=1+numsCount.get(nums[r],0)
        while(len(numsCount)>k):
            numsCount[nums[l]]-=1
            if numsCount[nums[l]]==0:
                numsCount.pop(nums[l])
            else:
                return True
            l+=1
    return False

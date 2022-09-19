Find duplicates within a range ‘k’ in an array

Input: nums = [5, 6, 8, 2, 4, 6, 9]
k = 2
Ouput: False

l=0
for r in range(len(nums)):
    numsCount[nums[r]]=1+numsCount.get(nums[r],0)
    if (r-l+1)==k:
        numsCount[nums[l]]-=1
        if numsCount[nums[l]]==0:
            numsCount.pop(nums[l])
        else:
            return True
        l+=1
return False
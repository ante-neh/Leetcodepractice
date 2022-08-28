Count distinct absolute values in a sorted array

Input:  { -1, -1, 0, 1, 1, 1 }

Output: The total number of distinct absolute values is 2 (0 and 1)

count={}
for i in range(len(nums)):
    if nums[i] not in count and nums[i]>0:
        counter+=1
    count[i]=nums[i]
return counter
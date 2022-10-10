def count(nums):
    counter=0
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                counter+=1
    return counter
num=[-2,45,0,11,15]
print(count(num))

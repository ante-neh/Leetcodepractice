Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.

Just like the movement of air bubbles in the water that rise up to the surface, each element of the array move to the end in each iteration. Therefore, it is called a bubble sort.



for i in range(len(nums)):
    for j in range(i+1,len(nums)-1-i):
        if nums[i]>nums[j]:
            nums[j],nums[l]=nums[l],nums[j]
return nums
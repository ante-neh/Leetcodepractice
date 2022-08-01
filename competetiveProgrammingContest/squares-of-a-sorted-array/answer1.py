class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedNums=[]
        start,end=0,len(nums)-1
        while start<=end:
            if abs(nums[start])<abs(nums[end]):
                sortedNums.append(nums[end]**2)
                end-=1
            else:
                sortedNums.append(nums[start]**2)
                start+=1
        return sortedNums[::-1]
#space complexity O(n)
#time complexity O(n)
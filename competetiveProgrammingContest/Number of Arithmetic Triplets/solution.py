class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        i,j,k=0,1,2
        counter=0
        while i<len(nums) and j<len(nums) and k<len(nums):
            if nums[j]-nums[i]<diff:
                j+=1
            elif nums[j]-nums[i]>diff:
                i+=1
            else:
                if nums[k]-nums[j]<diff:
                    k+=1
                elif nums[k]-nums[j]>diff:
                    j+=1
                else:
                    counter+=1
                    k+=1
        return counter
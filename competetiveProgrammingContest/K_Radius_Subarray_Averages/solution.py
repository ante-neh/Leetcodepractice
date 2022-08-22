class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result=[]
        sum=l=0
        L=k
        if k==0:
            return nums
        elif k>len(nums):
            return [-1]*len(nums)
        for i in range(k):
            sum+=nums[i]
            result.append(-1)
        for r in range(k,len(nums)):
            sum+=nums[r]
            if (r-L)==k:
                result.append(sum//(r-l+1))
                sum-=nums[l]
                l+=1
                L+=1
        for i in range(L,len(nums)):
            result.append(-1)
        return result
    #time complexity O(n)
    #space complexity O(n)
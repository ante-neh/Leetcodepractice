class Solution:
    def getAverages(self, nums, k):
        sum=l=0
        L=k
        result=[-1]*len(nums)
        if k==0:
            return nums
        elif k>len(nums):
            return result
        for i in range(k):
            sum+=nums[i]
        for r in range(k,len(nums)):
            sum+=nums[r]
            if r-L==k:
                result[L]=sum//(r-l+1)
                sum-=nums[l]
                l+=1
                L+=1
        return result
sol=Solution()
num = [8]
k = 100000

print(sol.getAverages(num, k))
    #time complexity O(n)
    #space complexity O(n)
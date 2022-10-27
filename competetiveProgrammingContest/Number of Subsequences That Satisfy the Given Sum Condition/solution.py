class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        mod = 10**9 + 7
        r = n-1 
        for l in range(n):
            while l<=r and nums[l]+nums[r] > target:
                r-=1
            
            if l<=r and nums[l] + nums[r] <= target:
                res += pow(2,(r-l) , mod)
                res %= mod
        
        return res
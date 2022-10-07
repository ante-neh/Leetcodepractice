class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]&2==0:
                nums[i]=0
            else:
                nums[i]=1
        counter=0
        prefixSum={0:1}
        curSum=0
        for num in nums:
            curSum+=num
            diff=curSum-k
            counter+=prefixSum.get(diff,0)
            prefixSum[curSum]=1+prefixSum.get(curSum,0)
        return counter


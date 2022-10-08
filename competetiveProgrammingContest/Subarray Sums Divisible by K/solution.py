class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter,sum=0,0
        prefixDiv={0:1}
        for i in range(len(nums)):
            sum+=nums[i]
            quet=sum%k
            counter+=prefixDiv.get(quet,0)
            prefixDiv[quet]=1+prefixDiv.get(quet,0)
        return counter
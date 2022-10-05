class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        sum=0
        result=[]
        for i in range(len(nums)):
            sum+=nums[i]
            nums[i]=sum
        for query in queries:
            index=bisect.bisect_right(nums,query)
            result.append(index)
        return result
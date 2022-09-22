class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        result=0
        stack=[]
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        for i,num in enumerate(nums):
            newStart=i
            while stack and stack[-1][0]>num:
                val,startIndex=stack.pop()
                total=prefix[i]-prefix[startIndex]
                result=max(result,val*total)
                newStart=startIndex
            stack.append([num,newStart])
        for val,i in stack:
            total=prefix[len(nums)]-prefix[i]
            result=max(result,val*total)
        return result%(10**9+7)
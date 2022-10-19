class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix,postfix=[],[]
        sum,counter=0,0
        for i in range(len(nums)):
            sum+=nums[i]
            prefix.append(sum)
        sum=0
        for i in range(len(nums)-1,-1,-1):
            sum+=nums[i]
            postfix.append(sum)
        for i in range(len(postfix)-1):
            if prefix[i]>=postfix[len(nums)-2-i]:
                counter+=1
        return counter
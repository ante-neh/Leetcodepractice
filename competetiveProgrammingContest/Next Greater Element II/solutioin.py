class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result=[-1]*len(nums)
        stack=[]
        for i,num in enumerate(nums*2):
            while stack and stack[-1][0]<num:
                val,index=stack.pop()
                result[index]=num
            if i<len(nums):
                stack.append([num,i])
        return result
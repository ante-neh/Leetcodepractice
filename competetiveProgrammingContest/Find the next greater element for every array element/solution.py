class Solution:
    def findNextGreaterElements(self,nums):
        result=[-1]*len(nums)
        stack=[]
        for i,num in enumerate(nums):
            while stack and stack[-1][0]<num:
                val,index=stack.pop()
                result[index]=num
            stack.append([num,i])
        return result

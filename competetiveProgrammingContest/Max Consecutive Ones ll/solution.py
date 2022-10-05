class Solution:
    def findMaxConsecutiveOnes(self,nums:List[int])->int:
        left=-1
        ones=0
        maxLen=0
        for num in nums:
            if num==1:
                ones+=1
            else:
                maxLen=max(maxLen,left+1+ones)
                left,ones=ones,0
        return max(maxLen,left+ones+1)
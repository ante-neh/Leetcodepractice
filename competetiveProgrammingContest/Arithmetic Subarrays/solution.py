class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i in range(len(l)):
            num=sorted(nums[l[i]:r[i]+1])
            diff=num[1]-num[0]
            flag=True
            for i in range(1,len(num)):
                if num[i]-num[i-1]!=diff:
                    flag=False
            if flag:
                res.append(True)
            else:
                res.append(False)        
        return res
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res=[]
        stack=[]
        
        for val in reversed(nums2):
            while stack and val>=stack[-1]:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(val)
        
        res.reverse()
        ans=[]
        
        for val in nums1:
            ind=nums2.index(val)
            ans.append(res[ind])
        return ans
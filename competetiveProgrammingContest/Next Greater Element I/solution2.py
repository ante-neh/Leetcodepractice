class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsIndex={}
        stack=[]
        ans=[-1]*len(nums1)
        for num in nums2:
            while stack and stack[-1]<num:
                val=stack.pop()
                numsIndex[val]=num
            stack.append(num)
        for i in range(len(nums1)):
            if nums1[i] in numsIndex:
                ans[i]=numsIndex[nums1[i]]
        return ans
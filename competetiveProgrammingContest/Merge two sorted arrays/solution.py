class Solution:
    def mergeTwoSortedArray(self,nums1,nums2):
        merged=[]
        l1,l2=0,0
        while l1<len(nums1) and l2<len(nums2):
            if nums1[l1]<nums2[l2]:
                merged.append(nums1[l1])
                l1+=1
            else:
                merged.append(nums2[l2])
                l2+=1
        while l1<len(nums1):
            merged.append(nums1[l1])
            l1++1
        while l2<len(nums2):
            merged.append(nums2[l2])
            l2+=1
        return merged

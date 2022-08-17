class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L,R,r=m-1,n+m-1,n-1
        while r>-1:
            if nums2[r]>nums1[L]:
                nums1[R]=nums2[r]
                R-=1
            elif nums2[r]<=nums1[L]:
                while nums2[r]<nums1[L]:
                    nums1[R]=nums1[L]
                    L-=1
                    R-=1
                nums1[L+1]=nums2[r]
            r-=1

#time complexity O(n)
#space complexity O(1)
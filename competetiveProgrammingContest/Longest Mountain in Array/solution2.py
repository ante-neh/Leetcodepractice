class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)-1
        res,l=0,0
        while l<n:
            if l<n and arr[l]<arr[l+1]:
                a,b=1,0
                while l<n and arr[l]<arr[l+1]:
                    a+=1
                    l+=1
                while l<n and arr[l]>arr[l+1]:
                    b+=1
                    l+=1
                if b!=0 and a+b>=3:
                    res=max(res,a+b)
            else:
                l+=1
        return res
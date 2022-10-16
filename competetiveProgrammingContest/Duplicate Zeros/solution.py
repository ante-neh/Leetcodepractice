class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l=0
        while l<len(arr)-1:
            if arr[l]==0:
                arr.insert(l+1,0)
                del arr[len(arr)-1]
                l+=2
            else:
                l+=1
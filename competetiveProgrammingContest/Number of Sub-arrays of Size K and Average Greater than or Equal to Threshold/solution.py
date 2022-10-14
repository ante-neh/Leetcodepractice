class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l,counter=0,0
        sum=0
        for r in range(len(arr)):
            sum+=arr[r]
            if r-l+1==k:
                if sum/k>=threshold:
                    counter+=1
                sum-=arr[l]
                l+=1
        return counter
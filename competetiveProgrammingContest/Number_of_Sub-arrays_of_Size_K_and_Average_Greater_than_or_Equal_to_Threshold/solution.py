class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum=0
        counter=0
        l=0
        for r in range(len(arr)):
            sum+=arr[r]
            if (r-l+1)==k:
                if sum/k>=threshold:
                    counter+=1
                sum-=arr[l]
                l+=1
        return counter
    #time complexity O(n)
    #space complexity O(1)
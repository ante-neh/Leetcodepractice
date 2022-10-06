class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefixSum=[]
        totalSum,sum=0,0
        for i in range(len(arr)):
            sum+=arr[i]
            prefixSum.append(sum)
            totalSum=sum
        for i in range(2,len(arr),2):
            j=0
            while j+i<len(arr):
                if j==0:
                    totalSum+=prefixSum[i]
                else:
                    totalSum+=prefixSum[i+j]-prefixSum[j-1]
                j+=1
        return totalSum
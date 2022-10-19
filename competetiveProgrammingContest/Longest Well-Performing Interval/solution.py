class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        count,sum=0,0
        prefixSum={}
        for i in range(len(hours)):
            if sum not in prefixSum:
                prefixSum[sum]=i
            if hours[i]>8:
                sum+=1
            else:
                sum-=1
            target=sum-1
            if target in prefixSum:
                count=max(count,i-prefixSum[target]+1,i+1 if sum>0 else 0)
        return count
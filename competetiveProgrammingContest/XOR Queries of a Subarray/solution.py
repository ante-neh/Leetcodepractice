class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        for i in range(1,len(arr)):
            arr[i]=arr[i]^arr[i-1]
        arr=[0]+arr
        for left,right in queries:
            res.append(arr[right+1]^arr[left])
        return res
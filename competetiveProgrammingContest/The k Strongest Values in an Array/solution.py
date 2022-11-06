class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = (len(arr) - 1) // 2
        median = arr[m]
        
        arr.sort(key = lambda n:(abs(n-median),n), reverse = True)
        
        return arr[:k]
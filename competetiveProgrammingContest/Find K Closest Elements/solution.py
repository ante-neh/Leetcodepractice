class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr=sorted(arr,key=lambda i:abs(i-x))
        arr=arr[:k]
        arr=sorted(arr)
        return arr
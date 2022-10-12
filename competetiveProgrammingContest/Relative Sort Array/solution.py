class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        countIndex={}
        for index,val in enumerate(arr2):
            countIndex[val]=index
        arr1.sort(key=lambda val:countIndex.get(val,max(countIndex)+val))
        return arr1
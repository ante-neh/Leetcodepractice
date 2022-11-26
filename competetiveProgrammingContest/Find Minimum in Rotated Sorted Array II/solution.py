class Solution:
    def findMin(self, nums: List[int]) -> int:
        newNums = []
        for i in nums:
            if not i in newNums:
                newNums.append(i)
                
        if len(newNums) == 1:
            return newNums[0]
        
        l, r = 0, len(newNums) - 1
        
        if newNums[r] > newNums[0]:
            return newNums[0]
        
        while l <= r:
            m = l + (r - l) // 2
            
            if newNums[m] > newNums[m + 1]:
                return newNums[m + 1]
            
            if newNums[m - 1] > newNums[m]:
                return newNums[m]
            
            if newNums[m] > newNums[0]:
                l = m + 1
            
            else:
                r = m - 1
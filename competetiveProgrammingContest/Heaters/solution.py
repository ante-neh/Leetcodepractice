class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l = 0
        res = 0
        
        for house in houses:
            while l + 1 < len(heaters) and abs(heaters[l]-house) >= abs(heaters[l+1]-house):
                l += 1
            res = max(abs(heaters[l]-house), res)
            
        return res
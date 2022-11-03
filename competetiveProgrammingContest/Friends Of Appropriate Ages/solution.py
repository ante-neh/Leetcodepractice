class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0
        
        ages.sort()
        
        l, r, count = 0, 0, 0
        
        for age in ages:
            while l < len(ages) and ages[l] <= 0.5 * age + 7:
                l += 1
            while r < len(ages) and ages[r] <= age:
                r += 1
            if r - 1 >= l:
                count += r - l - 1
        
        return count
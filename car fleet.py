class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        n = len(position)
        cars = [(position[i], (target - position[i])/speed[i]) for i in range(n)]
        
        cars.sort(reverse = True)
        
        ans = 0
        timeToReach = 0
        
        for (_, time) in cars: 
            if time > timeToReach: 
                ans += 1
                timeToReach = time
    
        return ans
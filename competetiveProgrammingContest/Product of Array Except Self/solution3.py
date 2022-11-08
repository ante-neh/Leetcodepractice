class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * (n + 2)
        
        for booking in bookings:
            seats[booking[0]] += booking[2]
            seats[booking[1] +1] -= booking[2]
            
        for i in range(1,len(seats)):
            seats[i] += seats[i-1]
            
        return seats[1:-1]
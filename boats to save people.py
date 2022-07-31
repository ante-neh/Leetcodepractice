class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter=0
        people.sort()
        start,end=0,len(people)-1
        while start<=end:
            counter+=1
            if people[start]+people[end]<=limit:
                start+=1
            end-=1
        return counter
    #time complexity O(nlogn)
    #space complexity O(1)
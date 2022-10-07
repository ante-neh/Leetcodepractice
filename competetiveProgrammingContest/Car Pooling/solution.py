class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lastDrop=-1
        for trip in trips:
            lastDrop=max(lastDrop,trip[2])
        events=[0]*(lastDrop+1)
        for trip in trips:
            events[trip[1]]+=trip[0]
            events[trip[2]]-=trip[0]
        if events[0]>capacity:
            return False
        for i in range(1,len(events)):
            events[i]+=events[i-1]
            if events[i]>capacity:
                return False
        return True
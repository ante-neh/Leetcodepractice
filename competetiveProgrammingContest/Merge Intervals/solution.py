class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        key=intervals[0]
        res=[key]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=key[1] and intervals[i][1]>=key[1]:
                res[-1][1]=intervals[i][1]
            elif intervals[i][0]>key[1]:
                res.append(intervals[i])
            key=res[-1]
        return res
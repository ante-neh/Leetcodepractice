class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda point:point[0])
        widestVerticalArea = float('-inf')
        
        for i in range(1,len(points)):
            widestVerticalArea = max(widestVerticalArea, points[i][0] - points[i-1][0])
            
        return widestVerticalArea
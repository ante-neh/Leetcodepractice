class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        visited=[0 for i in range(52)]
        for i in ranges:
            a,b=i
            visited[a]+=1
            visited[b+1]-=1
        for i in range(1,52):
            visited[i]+=visited[i-1]
        for i in range(left,right+1):
            if visited[i]<=0:
                return False
        return True
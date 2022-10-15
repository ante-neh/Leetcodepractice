class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer=[]
        cIndex=float('-inf')
        for i in range(len(s)):
            if s[i]==c:
                cIndex=i
            answer.append(abs(i-cIndex))
        cIndex=float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i]==c:
                cIndex=i
            answer[i]=min(answer[i],abs(i-cIndex))
        return answer
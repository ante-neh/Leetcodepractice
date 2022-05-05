class Solution:
    def hIndex(self, citations) -> int:
        citations.sort(reverse=True)
        answer=0
        for i,j in enumerate(citations):
            answer=max(answer,min(i+1,j))
            
        return answer
        
     #time complexity O(n)
    #space complexity O(1)
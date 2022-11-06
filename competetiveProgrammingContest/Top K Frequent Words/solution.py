class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsFreq = {}
        
        for word in words:
            wordsFreq[word] = 1 + wordsFreq.get(word, 0)
            
        wordsFreq = sorted(wordsFreq.items(), key = lambda items:(-items[1],items[0]))
        
        result = []
        for i in range(k):
            result.append(wordsFreq[i][0])
            
        return result
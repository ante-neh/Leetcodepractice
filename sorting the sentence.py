class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words = sorted(words, key=lambda x : x[-1])
        words = map(lambda x : x[:-1], words)
        return " ".join(words)
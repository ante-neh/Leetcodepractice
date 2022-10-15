class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2=0,0
        merged=[]
        while l1<len(word1) and l2<len(word2):
            merged.append(word1[l1])
            merged.append(word2[l2])
            l1+=1
            l2+=1
        if l1<len(word1):
            merged.append(word1[l1:])
        elif l2<len(word2):
            merged.append(word2[l2:])
        return ''.join(merged)
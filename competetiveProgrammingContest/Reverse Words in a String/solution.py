class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        newS=[]
        for word in s:
            if word!="":
                newS.append(word)
        newS=newS[::-1]
        return ' '.join(newS)
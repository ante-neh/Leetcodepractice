class Solution:
    def sortSentence(self, s: str) -> str:
        shufle=s.split(" ")
        final=""
        for i in range(len(shufle)):
            min=i
            for j in range(i+1,len(shufle)):
                if shufle[j][-1]<shufle[min][-1]:
                    min=j
            if min!=i:
                shufle[min],shufle[i]=shufle[i],shufle[min]
            final+=shufle[i][:-1]+' '
        return final[:-1]
        
       
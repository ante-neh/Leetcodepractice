class Solution:
    def sortSentence(self, s: str) -> str:
        shuffle=s.split(" ")
        result=""
        for i in range(len(shuffle)):
            minIndex=i
            for j in range(i+1,len(shuffle)):
                if shuffle[j][-1]<shuffle[minIndex][-1]:
                    minIndex=j
            shuffle[minIndex],shuffle[i]=shuffle[i],shuffle[minIndex]
            result+=shuffle[i][:-1]+" "
        return result[:-1]
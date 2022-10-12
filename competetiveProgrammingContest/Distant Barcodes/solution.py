class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        countFreq={}
        for i in range(len(barcodes)):
            countFreq[barcodes[i]]=1+countFreq.get(barcodes[i],0)
        countFreq=sorted(countFreq.items(),key=lambda item:item[1],reverse=True)
        indicies=list(range(0,len(barcodes),2))+list(range(1,len(barcodes),2))
        i=0
        for val,cnt in countFreq:
            while cnt>0:
                barcodes[indicies[i]]=val
                cnt-=1
                i+=1
        return barcodes
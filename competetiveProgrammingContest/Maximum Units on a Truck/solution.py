class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes,key=lambda item:item[1],reverse=True)
        maxUnits,i=0,0
        while truckSize>0 and i<len(boxTypes):
            if truckSize>boxTypes[i][0]:
                maxUnits+=boxTypes[i][0]*boxTypes[i][1]
                truckSize-=boxTypes[i][0]
            else:
                maxUnits+=truckSize*boxTypes[i][1]
                truckSize=0
            i+=1
        return maxUnits
            
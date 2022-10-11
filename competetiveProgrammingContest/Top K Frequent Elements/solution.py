class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq,res={},[]
        for num in nums:
            countFreq[num]=1+countFreq.get(num,0)
        countFreq=sorted(countFreq.items() ,key=lambda item:item[1],reverse=True)
        for i in countFreq:
            res.append(i[0])
            k-=1
            if k==0:
                return res
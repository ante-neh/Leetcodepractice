class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsCount={}
        l=0
        maxCollect=float('-inf')
        for r in range(len(fruits)):
            fruitsCount[fruits[r]]=1+fruitsCount.get(fruits[r],0)
            while len(fruitsCount)>2:
                fruitsCount[fruits[l]]-=1
                if fruitsCount[fruits[l]]==0:
                    fruitsCount.pop(fruits[l])
                l+=1
            maxCollect=max(maxCollect,r-l+1)
        return maxCollect
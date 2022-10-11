class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l,r=0,len(piles)-2
        maxCoins=0
        while l<r:
            maxCoins+=piles[r]
            r-=2
            l+=1
        return maxCoins
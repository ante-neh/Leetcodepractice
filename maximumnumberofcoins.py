class Solution:
    def maxCoins(self, piles) -> int:
        piles = sorted(piles)
        n = 0
        bob, me = 0, len(piles) - 2
        while bob < me:
            n += piles[me]
            me -= 2
            bob += 1
        return n
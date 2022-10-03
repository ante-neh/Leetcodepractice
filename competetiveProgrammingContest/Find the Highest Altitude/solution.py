class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum=[0]
        for i in range(len(gain)):
            prefixSum.append(prefixSum[i]+gain[i])
        return max(prefixSum)
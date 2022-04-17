class Solution:
    def minSetSize(self, arr) -> int:
        dp = {}
        
        for i in arr:
            dp[i] = 1 + dp.get(i, 0)

        dp = {k:v for k,v in sorted(dp.items(), key=lambda x: x[1], reverse=True)}
        
        elements_to_remove = 0
        n = len(arr)
        
        for i in dp:

            n -= dp[i]
            elements_to_remove += 1
            if n <= len(arr)//2:
                return elements_to_remove
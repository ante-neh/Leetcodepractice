class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def sumHourglass(i,j):
            return sum(grid[i - 1][j - 1 : j + 2]) + grid[i][j] + sum(grid[i + 1][j - 1 : j + 2])

        rows, cols = len(grid), len(grid[0])
        maxSum = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                maxSum = max(maxSum, sumHourglass(r, c))

        return maxSum
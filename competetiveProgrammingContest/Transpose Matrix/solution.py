class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        newMatrix = [[0] * r for _ in range(c)]

        for i in range(c):
            for j in range(r):
                newMatrix[i][j] = matrix[j][i]

        return newMatrix
class Solution:
    def spiralOrder(self, matrix):
        spiral_matrix = []
        while matrix:
            spiral_matrix.extend(matrix.pop(0))
            if not matrix:
                break
            spiral_matrix.extend(row.pop() for row in matrix if row)
            if not matrix:
                break
            spiral_matrix.extend(matrix.pop()[::-1])
            if not matrix:
                break
            spiral_matrix.extend(row.pop(0) for row in matrix[::-1]
                       if row)
        return spiral_matrix
    #time complexity O(n)
    #space complexity O(n)
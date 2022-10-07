class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix),len(matrix[0])
        self.prefix=[[0]*(cols+1) for r in range(rows+1)]
        for i in range(rows):
            prefixsum=0
            for j in range(cols):
                prefixsum+=matrix[i][j]
                above=self.prefix[i][j+1]
                self.prefix[i+1][j+1]=prefixsum+above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2=row1+1,col1+1,row2+1,col2+1
        bottomright=self.prefix[r2][c2]
        above=self.prefix[r1-1][c2]
        left=self.prefix[r2][c1-1]
        topleft=self.prefix[r1-1][c1-1]
        return bottomright-above-left+topleft
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells=[]
        for i in range(rows):
            for j in range(cols):
                cells.append([i,j])
        cells=sorted(cells,key=lambda item:abs(rCenter-item[0])+abs(cCenter-item[1]))
        return cells
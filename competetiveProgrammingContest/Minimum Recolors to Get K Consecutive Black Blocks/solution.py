class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        l=0
        minChanged=float('inf')
        for r in range(len(blocks)):
            if blocks[r]=='W':
                count+=1
            if r-l+1==k:
                minChanged=min(minChanged,count)
                if blocks[l]=='W':
                    count-=1
                l+=1
        return minChanged
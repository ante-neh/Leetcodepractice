class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for n in range(left,right+1):
            found=False
            for s,e in ranges:
                if n in range(s,e+1):
                    found=True
                    break
            if found==False:
                return False
        return True
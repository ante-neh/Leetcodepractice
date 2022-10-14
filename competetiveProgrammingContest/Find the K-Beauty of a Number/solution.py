class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num=str(num)
        count=l=0
        for r in range(len(s)):
            if r-l+1==k:
                div=num[l:r+1]
                if div!=0 and int(num)%div==0:
                    count+=1
                l+=1
        return count
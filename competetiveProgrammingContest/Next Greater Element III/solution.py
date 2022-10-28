class Solution:
    def nextGreaterElement(self, n: int) -> int:
        m=n
        n=list(str(n))
        i=len(n)-2
        while i>=0 and int(n[i+1])<=int(n[i]):
            i-=1
        if i>=0:
            j=len(n)-1
            while int(n[j])<=int(n[i]):
                j-=1
            n[i],n[j]=n[j],n[i]
        n[i+1:]=reversed(n[i+1:])
        n=int(''.join(n))
        return -1 if n<=m or n>2**31-1 else n
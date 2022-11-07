class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.000
        if n<0:
            half=self.myPow(1/x,-(n//2))
        else:
            half=self.myPow(x,(n//2))
        if n%2==0:
            return half*half
        else:
            return half*half*x
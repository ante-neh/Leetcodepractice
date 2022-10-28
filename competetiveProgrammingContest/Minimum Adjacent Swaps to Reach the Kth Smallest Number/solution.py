class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        #find the next permutation of num
        def nextPermutation():
            i=len(num)-2
            while i>=0 and num[i+1]<=num[i]:
                i-=1
            if i>=0:
                j=len(num)-1
                while num[j]<=num[i]:
                    j-=1
                num[i],num[j]=num[j],num[i]
            num[i+1:]=reversed(num[i+1:])
            return True
        num=list(num)
        #store deep copy of num 
        oldNum=num.copy()
        count=0
        #find the kth smallest permutation of num
        for i in range(k):
            nextPermutation()
        #count how many swaps needed
        for i in range(len(num)):
            if num[i]!=oldNum[i]:
                j=i+1
                #find the first number in oldNum that matches the current number in num
                while num[j]!=oldNum[i]:
                    j+=1
                #swap to its correct position
                while j!=i:
                    num[j],num[j-1]=num[j-1],num[j]
                    j-=1
                    count+=1
        return count
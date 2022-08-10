def findSmallestDifference(num1,num2):
    num1.sort()
    num2.sort()
    l,r=0,0
    minDiff=10000 #The maximum possible value in the arrays ,to get it see the constrant portion of the problem statement"
    while l<len(num1) and r<len(num2):
        sum=abs(num1[l]-num2[r])
        if sum<minDiff:
            minDiff=sum
        if num1[l]<num2[r]:
            l+=1
        else:
            r+=1
    return minDiff

#time complexity O(n)
#space complexity O(1)
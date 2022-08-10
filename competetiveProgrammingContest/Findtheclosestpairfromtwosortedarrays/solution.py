def printClosest(num1, num2,target):
    l,r=0,len(num2)-1
    diff=10000 #maximum number see the constrant portion of the problem
    while l<len(num1) and r>=0:
        sum=num1[l]+num2[r]
        if abs(sum-target)<diff:
            diff=abs((num1[l]+num2[r])-target)
            index1=l
            index2=r
        if sum<target:
            l+=1
        else:
            r-=1
    return [num1[l],num2[r]]
    
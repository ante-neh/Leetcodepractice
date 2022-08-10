def printClosest(num1, num2,target):
    l,r=0,len(num2)-1
    diff=10000 #the maximum possible array value plus one,to get see the constrant portion of the problem
    while l<len(num1) and r>=0:
        sum=num1[l]+num2[r]
        if abs(sum-target)<diff:
            diff=abs(sum-target)
            index1=l
            index2=r
        if sum<target:
            l+=1
        else:
            r-=1
    return [num1[index1],num2[index2]]


"""
Test case Example 

num1=[1,4,5,7]
num2=[10,20,30,40]
target=32
print(printClosest(num1, num2, target))

OutPut [1,30]
"""
def countSwaps(a):
    n=len(a)
    flag=0
    for i in range(n-1):
        for j in range(n-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                flag+=1
    message="Array is sorted in {} swaps."
    print(message.format(flag))
    print("First Element:",a[0])
    print("Last Element:",a[n-1])

nums=[3,2,1]
countSwaps(nums)
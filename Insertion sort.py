def insertionSort1(n, arr):
    for i in range(n):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
            print(*arr)
        arr[j+1]=temp
    print(*arr) 
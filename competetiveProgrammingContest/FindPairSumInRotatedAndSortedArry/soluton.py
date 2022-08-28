def findPairSum(arr, target):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            break
    l=(i+1)%len(arr)
    r=i
    while l!=r:
        if arr[l]+arr[r]==target:
            return True
        elif arr[l]+arr[r]<target:
            l=(l+1)%len(arr)
        else:
            r=(len(arr)+r-1)/len(arr)
    return False
#time complexity O(n)
#space complexity O(1)
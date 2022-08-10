def moveZerosToLeft(arr):
    l,r=len(arr)-2,len(arr)-1
    while l>=0 and r>=0:
        if arr[r]==0 and arr[l]!=0:
            arr[l],arr[r]=arr[r],arr[l]
        if arr[r]!=0:
            r-=1
        if l<=r or arr[l]==0:
            l-=1
    return arr
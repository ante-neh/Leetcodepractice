def countingSort(arr):
    countsort=[0]*100
    for i in range(len(arr)):
        countsort[arr[i]]+=1
    return countsort
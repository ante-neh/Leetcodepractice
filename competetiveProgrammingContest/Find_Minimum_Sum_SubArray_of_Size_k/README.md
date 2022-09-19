Find minimum Sum SubArray of size k

Input: arr = [10, 4, 2, 5, 6, 3, 8, 1] k = 3 
Output: 11

l=0
for r in range(len(arr)):
    sum+=arr[r]
    if r-l+1==k:
        minSum=min(sum,minSum)
        sum-=arr[l]
        l+=1
return minSum
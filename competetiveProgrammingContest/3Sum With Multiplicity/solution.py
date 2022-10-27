class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod=10**9+7
        count=0
        arr.sort()
        for i in range(len(arr)):
            T=target-arr[i]
            l,r=i+1,len(arr)-1
            while l<r:
                if arr[l]+arr[r]<T:
                    l+=1
                elif arr[l]+arr[r]>T:
                    r-=1
                elif arr[l]!=arr[r]:
                    left=right=1
                    while l+1<r and arr[l]==arr[l+1]:
                        left+=1
                        l+=1
                    while r-1>l and arr[r]==arr[r-1]:
                        right+=1
                        r-=1
                    count+=right*left
                    count%=mod
                    l,r=l+1,r-1
                else:
                    count+=(r-l+1)*(r-l)/2
                    count%=mod
                    break
        return int(count)
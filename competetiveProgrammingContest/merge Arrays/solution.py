n, m = map(int, input().split())
 
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
 
p1, p2 = 0, 0
mergedNums = []
 
while p1 < len(nums1) and p2 < len(nums2):
    if nums1[p1] < nums2[p2]:
        mergedNums.append(nums1[p1])
        p1 += 1
    
    else:
        mergedNums.append(nums2[p2])
        p2 += 1
 
while p1 < len(nums1):
    mergedNums.append(nums1[p1])
    p1 += 1
 
while p2 < len(nums2):
    mergedNums.append(nums2[p2])
    p2 += 1
 
print(*mergedNums)
def removeConsecutiveDuplicates(str):
    l,r=0,1
    str=list(str)
    while r<len(str):
        if str[r]!=str[r-1]:
            l+=1
            str[l]=str[r]
        r+=1
    return ''.join(str[:l+1])

#time complexity O(n)
#space complexity O(1)
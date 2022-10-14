def getLongestSubstring(s):
    vowels=['a','e','i','o','u']
    l,r=0,0
    maxLen=0
    while r<len(s):
        if s[r] not in vowels:
            r+=1
        else:
            r+=1
            l=r
        maxLen=max(maxLen,r-l)
    return maxLen
str = "codeforintelligentses"
print(getLongestSubstring(str))

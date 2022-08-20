def countAnagram(text, word):
    if len(word)>len(text):
        return 0
    textCount,wordCount={},{}
    for i in range(len(word)):
        wordCount[word[i]]=1+wordCount.get(word[i],0)
        textCount[text[i]]=1+textCount.get(text[i],0)
    counter=1 if wordCount==textCount else 0
    l=0
    for r in range(len(word),len(text)):
        textCount[text[r]]=1+textCount.get(text[r],0)
        textCount[text[l]]-=1
        if textCount[text[l]]==0:
            textCount.pop(text[l])
        l+=1
        if textCount==wordCount:
            counter+=1
    return counter
"""
Input:
text = "gotxxotgxdogt"
word = "got"

Output:3
"""
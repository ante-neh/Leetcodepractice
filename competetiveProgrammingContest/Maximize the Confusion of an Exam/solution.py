class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answerkeyCount={}
        maxLen,l=0,0
        for r in range(len(answerKey)):
            answerkeyCount[answerKey[r]]=1+answerkeyCount.get(answerKey[r],0)
            while (r-l+1)-max(answerkeyCount.values())>k:
                answerkeyCount[answerKey[l]]-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen
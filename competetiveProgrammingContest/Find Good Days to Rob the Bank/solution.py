class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n,goodDays=len(security),[]
        numDaysBefore,numDaysAfter=[1]*n,[1]*n
        for i in range(1,n):
            if security[i]<=security[i-1]:
                numDaysBefore[i]=numDaysBefore[i-1]+1
            else:
                continue
        for i in range(n-2,-1,-1):
            if security[i]<=security[i+1]:
                numDaysAfter[i]=1+numDaysAfter[i+1]
            else:
                continue
        for i in range(n):
            if numDaysBefore[i]>time and numDaysAfter[i]>time:
                goodDays.append(i)
        return goodDays
    
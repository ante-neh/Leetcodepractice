class Solution:
    def findOriginalArray(self, changed):
        if len(changed) <=1:
            return []
        n=(10 ** 5) + 1
        m=[0]*n
        if len(changed) % 2 != 0:
            return []
        for num in changed:
            m[num]+=1
    
        result=[]
		#If we only have 0s
        if m[0] == len(changed):
            mx=2
        else:
            mx=max(changed)
        for j in range(0,(mx//2)+1):
		#handle 0s
            if j == 0 and m[j] != 0:
                val=m[j]
                m[j]=0
                for _ in range(val//2):
                    result.append(j)
                    continue
			#All non zero cases
            if j !=0 and m[j] != 0:
				# IMP: check out of bounds  when searching for double
                if 2*j < n and m[2*j] != 0:
                    m[2*j]-=m[j]                    
                    for _ in range(m[j]):
                        result.append(j)  
                    m[j]=0
                else:
                    return []
        for j in range(0,mx+1):
            if m[j] != 0:
                return []
        return result
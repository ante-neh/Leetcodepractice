class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sOut,tOut=[],[]
        for char in s:
            if char=='#':
                if sOut:
                    sOut.pop()
            else:
                sOut.append(char)
        for char in t:
            if char=='#':
                if tOut:
                    tOut.pop()
            else:
                tOut.append(char)
        return sOut==tOut
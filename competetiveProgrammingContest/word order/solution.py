# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = []

for i in range(n):
    s.append(input())

sFreq = {}
for word in s:
    sFreq[word] = 1 + sFreq.get(word, 0)
    
print(len(sFreq))
print(*sFreq.values())
# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())

room = list(map(int,input().split()))
roomFreq = {}

for r in room:
    roomFreq[r] = 1 + roomFreq.get(r, 0)

for x, f in roomFreq.items():
    if f == 1:
        print(x)
def piling(blocks):
    l, r = 0, len(blocks) - 1
    while blocks:
        large = None
        if blocks[-1] > blocks[0]:
            large = blocks.pop()
            
        else:
            large = blocks.pop(0)
            
        if len(blocks) == 0:
            return "Yes"
        
        if blocks[-1] > large or blocks[0] > large:
            return "No"
        
for i in range(int(input())):
    noOfCubes = int(input())
    blocks = list(map(int, input().split()))
    print(piling(blocks)) 
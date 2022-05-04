class Solution:
    def maxArea(self, height) -> int:
        start,end,maxWater=0,len(height)-1,0
        while start<end:
            if height[start]<height[end]:
                minHeight = height[start]
                start+=1
            else:
                minHeight = height[end]
                end-=1
            maxWater = max(maxWater, (end-start+1)*minHeight)
        
        return maxWater
    #time complexity O(n)
    #space complexity O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxWater=0
        leftMax,rightMax=height[l],height[r]
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax,height[l])
                maxWater+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax,height[r])
                maxWater+=rightMax-height[r]
        return maxWater
    #time complexity O(n)
    #sapce complexity O(1)
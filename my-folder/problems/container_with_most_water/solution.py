class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        val = 0
        cur = 0
        while(l<r):
            cur = (r-l)*min(height[l],height[r])
            if cur>val:
                val = cur
            if height[l]<height[r]:
                l+=1
            else: 
                r-=1
        return val
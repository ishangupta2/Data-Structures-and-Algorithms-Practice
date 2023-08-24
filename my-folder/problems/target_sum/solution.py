class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
       
        def dfs(i, total, cache):
            if i >= len(nums) and total==target:
                return 1
            if (i, total) in cache:
                return cache[(i, total)]
            if i>= len(nums):
                return 0
            cache[(i, total)] =  dfs(i+1, total+nums[i], cache) 
            cache[(i, total)] += dfs(i+1, total-nums[i], cache)
             
            return cache[(i, total)]
        return dfs(0, 0, cache)

class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1
        temp = -100
        count = 0
        while(goal != 0):
            for r in range(goal, -1, -1):
                if r + nums[r] >= goal:
                    temp = r
            goal = temp
            count +=1
        return count
        
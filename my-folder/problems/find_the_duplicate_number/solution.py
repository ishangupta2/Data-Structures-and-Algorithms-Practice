class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if(s == f):
                break
        newSlow = 0
        while True:
            newSlow = nums[newSlow]
            s  = nums[s]
            if newSlow == s:
                return newSlow

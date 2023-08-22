class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            n = set()
            for d in dp:
                n.add(nums[i]+d)
                n.add(d)
            dp = n
        return target in dp
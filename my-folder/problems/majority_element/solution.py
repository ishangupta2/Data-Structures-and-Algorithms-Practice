class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        x = len(nums)
        return nums[x//2]

        
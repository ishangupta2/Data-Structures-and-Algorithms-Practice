class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        summ = 0
        for num in nums:
            if summ < 0:
                summ = num
            else:
                summ += num
            mx = max(summ, mx)
        return mx
                

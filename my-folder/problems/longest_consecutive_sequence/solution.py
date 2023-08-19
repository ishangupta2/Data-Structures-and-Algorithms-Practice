class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        mx = 0
        for num in nums:
            if num-1 not in numSet:
                lent = 1
                while(num+lent in numSet):
                    lent+=1
                mx = max(mx, lent)
        return mx



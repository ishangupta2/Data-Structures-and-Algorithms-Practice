class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curset, subset = [], []
        def helper(i, nums, curset, subset):
            if i>=len(nums):
                subset.append(curset.copy())
                return
            else:
                curset.append(nums[i])
                helper(i+1, nums, curset, subset)
                curset.pop()
                helper(i+1, nums, curset, subset)
        helper(0, nums, curset, subset)
        return subset

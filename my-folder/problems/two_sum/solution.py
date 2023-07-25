class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapDiff = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in mapDiff:
                return [i, mapDiff.get(diff)]
            mapDiff[n] = i
        return False
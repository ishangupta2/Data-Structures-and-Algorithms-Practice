class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefMap = {}
        prefMap[0] = 1
        cur = 0
        res = 0
        for num in nums:
            cur += num
            if cur-k in prefMap:
                res += prefMap[cur-k]
            prefMap[cur] = 1 + prefMap.get(cur, 0)
        return res



        
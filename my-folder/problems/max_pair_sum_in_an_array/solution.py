class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mp = {}
        res = -1
        for num in nums:
            dig = max(str(num))
            if dig in mp:
                res = max(res, num+mp[dig])
                mp[dig] = max(mp[dig], num)
            else:
                mp[dig] = num
            
        return res
        
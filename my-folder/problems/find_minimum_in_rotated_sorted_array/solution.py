class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = nums[0]
        while L<=R:
            mid = (L+R)//2
            res = min(nums[mid], res)
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                return res
            elif nums[L] > nums[mid]:
                R = mid-1
            else:
                L = mid+1
        return res
        
        
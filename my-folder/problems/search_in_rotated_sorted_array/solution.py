class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        while(L<=R):
            mid = (L+R)//2
            if nums[mid]==target:
                return mid
            if nums[L] < nums[mid] and target>=nums[L] and target<=nums[mid]:
                R=mid-1
            elif nums[mid] < nums[R] and (target < nums[mid] or target>nums[R]):
                R = mid-1
            else:
                L=mid+1
        return -1
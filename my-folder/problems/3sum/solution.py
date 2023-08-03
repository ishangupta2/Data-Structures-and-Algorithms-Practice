class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        sums = []
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                diff = nums[i]+nums[l]+nums[r]
                if diff == 0:
                    sums.append((nums[i], nums[l], nums[r]))                
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    
                elif diff > 0:
                    r-=1
                else:
                   l+=1
        return sums
                    

  

        
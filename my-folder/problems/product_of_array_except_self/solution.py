class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] 
        temp = pref[0]
        post = [1]
        for num in nums:
            temp = temp*num
            pref.append(temp)
        temp = post[0]
        for x in reversed(nums):
            temp*=x
            post.append(temp)
        post.reverse()
        prod = []
        for i in range(1, len(pref), 1):
            prod.append(pref[i-1]*post[i])
        return prod

            


        
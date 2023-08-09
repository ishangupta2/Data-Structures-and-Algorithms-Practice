class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0
        maxPos = collections.deque()
        stk = []
        for R in range(len(nums)):
           
            while(maxPos and nums[maxPos[-1]]<nums[R]):
                    maxPos.pop()
            maxPos.append(R)
            if maxPos[0]<L:
                maxPos.popleft()
            if R-L+1>=k:
                stk.append(nums[maxPos[0]])
                L = L+1

        return stk


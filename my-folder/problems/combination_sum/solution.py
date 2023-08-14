class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        def helper(i, target, candidates, cur, curcomb, cursum):
            if cursum>target or i>=len(candidates):
                return 
            elif cursum == target:
                cur.append(curcomb.copy())
            else:
                for j in range(i, len(candidates)):
                    curcomb.append(candidates[j])
                    cursum+=candidates[j]
                    helper(j, target, candidates, cur, curcomb, cursum)
                    cursum-=candidates[j]
                    curcomb.pop()

        helper(0,target, candidates, cur, [], 0)
        return cur
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        candidates.sort()
        def helper(i, target, candidates, cur, comb, su):
            if su == target:
                comb.append(cur.copy())
                return 
            if i>=len(candidates) or su>target:
                return
            else:
                cur.append(candidates[i])
                helper(i+1, target, candidates, cur, comb, su+candidates[i])
                cur.pop()
                while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                    i+=1
                helper(i+1, target, candidates, cur, comb, su)
        helper(0, target, candidates, [], comb, 0)
        return comb
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            nperm = []
            for p in perms:
                for i in range(len(p)+1):
                    cpy = p.copy()
                    cpy.insert(i, n)
                    nperm.append(cpy)
            perms = nperm
        return perms

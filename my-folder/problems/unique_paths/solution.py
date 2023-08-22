class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0]*m
        for r in range(n-1,-1,-1):
            cur = [0]*m
            cur[m-1] = 1
            for c in range(m-2,-1,-1):
                cur[c] = cur[c+1]+prev[c]
            prev = cur
        return prev[0]

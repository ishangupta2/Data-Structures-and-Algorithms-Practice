class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1),len(text2)
        dp = [0]*(M+1)
        for i in range(N):
            curRow = [0]*(M+1)
            for d in range(M):
                if text1[i] == text2[d]:
                    curRow[d+1] = 1+dp[d]
                else:
                    curRow[d+1] = max(dp[d+1], curRow[d])
            dp = curRow
        return dp[M]

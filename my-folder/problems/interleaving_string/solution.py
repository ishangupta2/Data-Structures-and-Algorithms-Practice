class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for r in range(len(s2),-1,-1):
                if i < len(s1) and s3[i+r]==s1[i] and dp[i+1][r]:
                    dp[i][r] = True
                if r<len(s2) and s3[i+r]==s2[r] and dp[i][r+1]:
                    dp[i][r] = True
        return dp[0][0]

    
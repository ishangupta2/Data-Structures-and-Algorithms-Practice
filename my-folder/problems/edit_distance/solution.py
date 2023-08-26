class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")]*(len(word2)+1) for i in range(len(word1)+1)]
        for j in range(len(word2)+1):
            cache[len(word1)][j] = len(word2)-j
        for d in range(len(word1)+1):
            cache[d][len(word2)] = len(word1)-d
        for r in range(len(word1)-1,-1,-1):
            for c in range(len(word2)-1,-1,-1):
                if word1[r]==word2[c]:
                    cache[r][c] = cache[r+1][c+1]
                else:
                    cache[r][c] = 1+ min(cache[r+1][c], cache[r][c+1], cache[r+1][c+1])
        return cache[0][0]



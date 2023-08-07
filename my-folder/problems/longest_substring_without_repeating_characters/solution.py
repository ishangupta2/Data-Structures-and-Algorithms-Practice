class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        dups = set()
        L = 0
        for R in range(len(s)):
            if s[R] in dups:
                while(s[R] in dups):
                    dups.remove(s[L])
                    L+=1
            length = max(R-L+1, length)
            dups.add(s[R])
        return length

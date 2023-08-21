class Solution:
    def countSubstrings(self, s: str) -> int:


        def helper(s, l, r):
            num = 0

            while(l>=0 and r<len(s) and s[l]==s[r]):
                num+=1
                l-=1
                r+=1
            return num
        mx = 0
        for r in range(len(s)):
            mx += helper(s, r, r)
            mx += helper(s, r, r+1)
        return mx


            
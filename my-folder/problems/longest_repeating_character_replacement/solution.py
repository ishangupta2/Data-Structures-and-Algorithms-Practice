class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        L = 0
        mx = 0
        for r in range(len(s)):
            mp[s[r]] = 1+ mp.get(s[r], 0)
            num = (r-L+1)-max(mp.values())
            if num > k:
                mp[s[L]] = mp[s[L]]-1
                L=L+1
            mx = max(mx, r-L+1)
        return mx





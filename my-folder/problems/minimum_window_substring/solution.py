class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        mp1 = Counter(t)
        mp2 = {}
        L = 0
        curMin = float("infinity")
        resLen = [-1,-1]
        have, need = 0, len(mp1)
        for R in range(len(s)):
            if s[R] in mp1:
                mp2[s[R]] = 1 + mp2.get(s[R], 0)
                if mp2[s[R]] == mp1[s[R]]:
                    have+=1
            while have == need:
                if R-L+1<curMin:
                    curMin = R-L+1
                    resLen = [L, R]
                if s[L] in mp1:
                    mp2[s[L]]-=1
                    if mp2[s[L]] < mp1[s[L]]:
                        have-=1
                L = L+1
            l, r = resLen
        return s[l: r+1] if curMin != float("infinity") else ""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indx = 0
        if not s:
            return True
        if not t or len(t)<len(s):
            return False
        for char in t:
            if char == s[indx]:
                indx+=1
            if indx==len(s):
                return True
        return False
        
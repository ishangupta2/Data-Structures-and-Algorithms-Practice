class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = 0
        m = strs[0]
        for i in range(len(m)):
            curChar = m[i]
            for s in strs:
                if len(s)<=i or s[i]!=m[i]:
                        return m[0:pref]
            pref += 1


        return m[0:pref]
        
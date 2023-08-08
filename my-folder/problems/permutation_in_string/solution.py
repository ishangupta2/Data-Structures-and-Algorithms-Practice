class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        mp = Counter(s1)
        mp2 = {}
        if len(s1) > len(s2):
            return False
        for r in range(len(s2)):
            char = s2[r]
            if char in mp2:
                mp2[char] = mp2[char]+1
            if char not in mp2:
                mp2[char] = 1
            if mp2 == mp:
                return True
            elif r-L+1==len(s1):
                mp2[s2[L]] = mp2[s2[L]]-1
                if mp2[s2[L]] == 0:
                    mp2.pop(s2[L])
                L+=1
        return False

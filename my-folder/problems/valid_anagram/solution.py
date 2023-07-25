class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     if len(s)!=len(t):
        return False
     
     maps = {}
     map2 = {}
     for i in range(len(s)):
         maps[s[i]] = 1 + maps.get(s[i], 0)
         map2[t[i]] = 1 + map2.get(t[i], 0)
     return maps==map2


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {2: ("a","b","c"), 3: ("d", "e", "f"), 4:("g","h","i"), 5: ("j","k","l"), 6: ("m","n","o"), 7:("p","q","r","s"), 8: ("t", "u", "v"), 9: ("w","x","y","z")}
        fin = []
        def d(digits, ind, cur, fin, mp):
            if ind >= len(digits):
                sep = ""
                fin.append(sep.join(cur.copy()))
                return
            else:
                for char in mp[int(digits[ind])]:
                    cur.append(char)
                    d(digits, ind+1, cur, fin, mp)
                    cur.pop()
        if not digits:
            return []
        d(digits, 0, [], fin, mp)
        return fin

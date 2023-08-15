class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def isPalindrome(str, i, b):
            l, r = i, b
            while l<r:
                    if str[l]!=str[r]:
                        return False
                    else:
                        l+=1
                        r-=1
            return True
        def helper(i):
            if i>=len(s):
              res.append(part.copy())
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    helper(j+1)
                    part.pop()
        helper(0)
        return res

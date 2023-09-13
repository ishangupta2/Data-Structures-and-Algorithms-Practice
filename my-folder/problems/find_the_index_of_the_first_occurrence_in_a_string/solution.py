class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        word, L = deque(), 0
        if len(haystack)<len(needle):
            return -1
        for R in range(len(haystack)):
            if R-L+1>len(needle):
                word.popleft()
                L += 1
            word.append(haystack[R])
            if ''.join(word) == needle:
                print(word)
                return L
        return -1

        
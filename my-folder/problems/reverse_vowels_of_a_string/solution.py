class Solution:
    def reverseVowels(self, s: str) -> str:
        stk = []
        s = list(s)
        vowels = ('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U')
        for i in range(len(s)):
            if s[i] in vowels:
                stk.append(i)
        l, r = 0, len(stk)-1
        while(l<r and stk):
            num1, num2 = stk[l], stk[r]
            temp = s[num1]
            s[num1] = s[num2]
            s[num2] = temp
            l+=1
            r-=1
        return ''.join(s)

        
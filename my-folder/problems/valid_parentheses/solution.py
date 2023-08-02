class Solution:
    def isValid(self, s: str) -> bool:
        parenth = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if(char in parenth):
                if stack and stack[-1] == parenth[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

            
                
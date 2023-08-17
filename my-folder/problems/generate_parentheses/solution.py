class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(tl, l, c, strin):
            if c == tl and l==tl:
                stk.append(strin)
                return
            if tl<c or tl<l:
                return
            if c>l:
                return
            elif c==l:
                strin+="("
                dfs(tl, l+1, c, strin)
            elif c<l:
                dfs(tl, l+1, c, strin+ "(")
                dfs(tl, l, c+1, strin+")")
        stk = []
        dfs(n, 1, 0, "(")
        return stk
            

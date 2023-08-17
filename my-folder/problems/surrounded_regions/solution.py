class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        def dfs(r, c, visit):
            if((r,c) in visit or min(r,c)<0 or r== R or c == C or board[r][c] == 'X'):
                return
            visit.add((r,c))
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)
        visit = set()
        for r in range(R):
            dfs(r, 0, visit)
            dfs(r, C-1, visit)
        for c in range(C):
            dfs(0, c, visit)
            dfs(R-1, c, visit)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O' and (r,c) not in visit:
                    board[r][c] = 'X'





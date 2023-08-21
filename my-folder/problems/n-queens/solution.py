class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pdag = set()
        ndag = set()
        res = []
        board = [["."] * n for i in range(n)]
        def b(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for i in range(n):
                    if i in cols or (r+i) in pdag or (r-i) in ndag:
                        continue
                    cols.add(i)
                    pdag.add(r+i)
                    ndag.add(r-i)
                    board[r][i] = "Q"
                    b(r+1)
                    cols.remove(i)
                    pdag.remove(r+i)
                    ndag.remove(r-i)
                    board[r][i] = "."
        b(0)
        return res

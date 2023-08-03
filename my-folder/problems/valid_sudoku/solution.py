class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                elif num in rows[r]:
                    return False
                elif num in cols[c]:
                    return False
                elif num in squares[r//3,c//3]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[r//3,c//3].add(num)
        return True

                

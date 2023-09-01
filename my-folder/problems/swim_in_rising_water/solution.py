class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        direc = [[0,-1], [0,1], [1,0], [-1,0]]
        visit = set()
        visit.add((0,0))
        while minHeap:
            w, r, c = heapq.heappop(minHeap)
            if r == R-1 and c == R-1:
                return w
            for up, down in direc:
                row = r+up
                col = c+down
                if (row, col) in visit or min(row,col)<0 or row==R or col==R:
                    continue
                visit.add((row, col))
                heapq.heappush(minHeap, [max(w, grid[row][col]), row, col])


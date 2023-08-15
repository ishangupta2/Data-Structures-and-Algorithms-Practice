class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      def dfs(r, c, visit):
         R, C = len(grid), len(grid[0])
         if min(r,c)<0 or r==R or c==C or (r,c) in visit or grid[r][c] == '0':
             return
         visit.add((r,c))
         dfs(r+1, c, visit)
         dfs(r-1, c, visit)
         dfs(r, c+1, visit)
         dfs(r, c-1, visit)

      count = 0
      visit = set()
      for r in range(len(grid)):
          for c in range(len(grid[r])):
             if grid[r][c] == '1' and (r,c) not in visit:
                dfs(r, c, visit)
                count+=1
      return count
        
class Solution:
    def maxTrailingZeros(self, grid) -> int:
        #backtracking
        max_trailing_zeroes = 0
        for row in range(grid):
            for col in range(grid[0]):
                
                max_trailing_zeroes = max(self.dfs(self,grid,row,col),max_trailing_zeroes)

    
    def dfs(self,grid,row,col):

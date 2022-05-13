from collections import deque
class Solution:
    def hasValidPath(self, grid) -> bool:
        
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                result = self.bfs()
                if result:
                    return result

        return False

    def backtrack(self,grid,current_path,result,coord):
        
        r,c = coord[0],coord[1]
        current_path.append(grid[])
        

    #function returns Boolean if it can reach final destination
    def check_valid(self):
        
        
        
        return None

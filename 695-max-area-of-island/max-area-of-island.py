class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid,i,j)
                    max_area = max(max_area,area)
        return max_area
    def dfs(self,grid,visit,record):
        if(
            visit < 0
            or record < 0
            or visit>=len(grid)
            or record>=len(grid[0])
            or grid[visit][record] == 0
        ):
            return 0
        grid[visit][record] = 0
        return(
        1+self.dfs(grid,visit+1,record)
        +self.dfs(grid,visit-1,record)
        +self.dfs(grid,visit,record+1)
        +self.dfs(grid,visit,record-1))
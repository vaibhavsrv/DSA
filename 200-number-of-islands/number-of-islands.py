class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        if not grid:
            return 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    count += 1
        return count
    def dfs(self,grid,visit,record):
        if(
            visit < 0
            or record < 0
            or visit>=len(grid)
            or record>=len(grid[0])
            or grid[visit][record] != "1"
        ):
            return
        grid[visit][record] = "0"
        self.dfs(grid,visit+1,record)
        self.dfs(grid,visit-1,record)
        self.dfs(grid,visit,record+1)
        self.dfs(grid,visit,record-1)
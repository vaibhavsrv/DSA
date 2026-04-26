class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        def dfs(r,c,parentR,parentC,char):
            visited[r][c] = True
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r + dr , c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    if not visited[nr][nc]:
                        if dfs(nr, nc, r, c, char):
                            return True

                    elif (nr,nc) != (parentR,parentC):
                            return True

            return False

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if dfs(i,j,-1,-1,grid[i][j]):
                        return True
        return False
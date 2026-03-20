class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        result = [[0] * (n-k+1) for _ in range(m-k+1)]

        for i in range(m-k+1):
            for j in range(n-k+1):
                solve = sorted(set(
                        grid[x][y]
                        for x in range(i,i+k)
                        for y in range(j,j+k)
                    ))
                if len(solve) <= 1:
                    result[i][j] = 0
                else:
                    result[i][j] = min(solve[p+1] - solve[p] for p in range(len(solve) - 1))
        return result
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        answer = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = grid[i][j] + dp[i][j+1] + dp[i+1][j] - dp[i][j]
                if dp[i+1][j+1] <= k:
                    answer += 1
        return answer
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j] = 1
        for x in range(1,m):
            for y in range(1,n):
                dp[x][y] = dp[x-1][y]+dp[x][y-1]
        return dp[-1][-1]
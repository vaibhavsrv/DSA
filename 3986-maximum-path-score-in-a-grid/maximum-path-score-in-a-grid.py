class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        score = {0: 0, 1: 1, 2: 2}
        cost = {0: 0, 1: 1, 2: 1}

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        start_cost = cost[grid[0][0]]
        if start_cost <= k:
            dp[0][0][start_cost] = score[grid[0][0]]

        for i in range(m):
            for j in range(n):
                for costUSED in range(k + 1):
                    if dp[i][j][costUSED] == -1:
                        continue

                    c_score = dp[i][j][costUSED]

                    # Down
                    if i + 1 < m:
                        nc = costUSED + cost[grid[i+1][j]]
                        if nc <= k:
                            ns = c_score + score[grid[i+1][j]]
                            dp[i+1][j][nc] = max(dp[i+1][j][nc],ns)

                    # Right
                    if j + 1 < n:
                        nc = costUSED + cost[grid[i][j+1]]
                        if nc <= k:
                            ns = c_score + score[grid[i][j+1]]
                            dp[i][j+1][nc] = max(dp[i][j+1][nc],ns)

        return max(dp[m-1][n-1])
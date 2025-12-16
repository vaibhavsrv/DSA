class Solution:
    def solve(self, i, j, dungeon, dp):
        m = len(dungeon)
        n = len(dungeon[0])

        if i == m - 1 and j == n - 1:
            return max(1, 1 - dungeon[i][j])

        if i >= m or j >= n:
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
        right = self.solve(i, j + 1, dungeon, dp)
        left = self.solve(i + 1, j, dungeon, dp)

        minHealth = min(right, left) - dungeon[i][j]
        dp[i][j] = max(1, minHealth)

        return dp[i][j]
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[-1] * n for _ in range(m)]
        return self.solve(0, 0, dungeon, dp)
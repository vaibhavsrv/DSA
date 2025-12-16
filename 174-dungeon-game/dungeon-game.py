class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        def solve(minHealth):
            dp = [[-1] * n for _ in range(m)]

            dp[0][0] = minHealth + dungeon[0][0]
            if dp[0][0] <= 0:
                return False

            for i in range(m):
                for j in range(n):
                    if dp[i][j] <= 0:
                        continue

                    if i + 1 < m:
                        dp[i + 1][j] = max(
                            dp[i + 1][j],
                            dp[i][j] + dungeon[i + 1][j]
                        )

                    if j + 1 < n:
                        dp[i][j + 1] = max(
                            dp[i][j + 1],
                            dp[i][j] + dungeon[i][j + 1]
                        )

            return dp[m - 1][n - 1] > 0

        left, right = 1, 10**7
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if solve(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

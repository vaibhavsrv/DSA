
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            root = int(i ** 0.5)

            for j in range(1, root + 1):
                square = j * j

                if not dp[i - square]:
                    dp[i] = True
                    break

        return dp[n]
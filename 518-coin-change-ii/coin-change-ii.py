class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def solve(n, amount):
            if amount == 0:
                return 1
            if amount < 0 or n == 0:
                return 0

            if (n, amount) in dp:
                return dp[(n, amount)]

            skip = solve(n - 1, amount)
            take = solve(n, amount - coins[n - 1])

            dp[(n, amount)] = skip + take
            return dp[(n, amount)]

        return solve(len(coins), amount)

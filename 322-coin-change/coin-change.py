class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10**9
        dp = {}

        def solve(n,amount):
            if amount == 0:
                return 0
            if n == 0:
                return INF

            if (n,amount) in dp:
                return dp[(n,amount)]

            skip = solve(n-1,amount)
            take = INF

            if coins[n-1] <= amount:
                take = 1 + solve(n, amount - coins[n-1])
            dp[(n,amount)] = min(skip,take)

            return dp[(n,amount)]
        res = solve(len(coins),amount)
        if res >= INF:
            return -1
        else:
            return res
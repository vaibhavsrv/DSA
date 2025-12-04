class Solution:

    dp = [-1] * 31

    def fib(self, n: int) -> int:
        '''if n <= 1:
            return n
        f = [0] * (n + 1)

        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]'''

        if n <= 1:
            return n

        start = self.dp[n-1] if self.dp[n - 1] != -1 else self.fib(n-1)
        end = self.dp[n-2] if self.dp[n-2] != -1 else self.fib(n-2)

        self.dp[n] = start + end
        return self.dp[n]
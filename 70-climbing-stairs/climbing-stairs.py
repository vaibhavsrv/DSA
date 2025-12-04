class Solution:
    def climbStairs(self, n: int) -> int:
        '''if n <= 1:
            return n

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]'''

        '''start = self.dp[n-1] if self.dp[n - 1] != -1 else self.climbStairs(n-1)
        end = self.dp[n-2] if self.dp[n-2] != -1 else self.climbStairs(n-2)

        self.dp[n] = start + end
        return self.dp[n]
        '''
        if n == 0:
            return 1

        if n == 1:
            return 1
        prev, curr = 1,1

        for i in range(2,n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr


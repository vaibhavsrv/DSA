class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def solve(a):
            if a == 0:
                return 0

            if a in memo:
                return memo[a]
            
            min_count = float('inf')
            i = 1
            while i * i <= a:
                min_count = min(min_count,1+solve(a-i*i))
                i+=1

            memo[a] = min_count
            return memo[a]

        return solve(n)
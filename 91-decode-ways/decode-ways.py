class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def dp(index, memo: dict):
            if index == n:
                return 1
            if s[index] == "0":
                return 0
            if index not in memo:
                memo[index] = 0
                if 1 <= int(s[index]) <= 9:
                    memo[index] += dp(index+1, memo)
                if 10 <= int(s[index:index+2]) <= 26:
                    memo[index] += dp(index+2, memo)
            return memo[index]
        return dp(0, {})
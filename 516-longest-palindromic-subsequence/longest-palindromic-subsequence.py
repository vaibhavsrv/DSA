class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def solve(i,j):
            if i > j :
                return 0
            if i == j:
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i] == s[j]:
                dp[(i,j)] = 2 + solve(i+1,j-1)
            else:
                dp[(i,j)] = max(solve(i+1,j),solve(i,j-1))
            return dp[(i,j)]

        return solve(0,len(s)-1)
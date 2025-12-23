class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def solve(i,j):
            n,m = len(text1),len(text2)

            if i >= n or j >= m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            if text1[i] == text2[j]:
                dp[(i,j)] = 1 + solve(i+1,j+1)
            else:
                dp[(i,j)] = max(solve(i+1,j),solve(i,j+1))
            
            return dp[(i,j)]
        return solve(0,0)
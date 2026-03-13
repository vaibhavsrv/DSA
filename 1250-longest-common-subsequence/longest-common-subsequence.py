class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # THIS IS THE PURE RECURSIVE CODE FOR LCS , THROWING TLEEEEE
        # NOW WITH MEMO
        memo = {}
        def dp(i,j):
            if i == 0 or j == 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i-1] == text2[j-1]:
                memo[(i,j)] = 1 + dp(i-1,j-1)
            else:
                memo[(i,j)] =  max(dp(i,j-1),dp(i-1,j))
            return memo[(i,j)]
        return dp(len(text1),len(text2))      
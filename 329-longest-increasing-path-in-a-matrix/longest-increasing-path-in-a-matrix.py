class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix),len(matrix[0])
        if not matrix or not matrix[0]:
            return 0
        dp = [[0] *  m for _ in range(n)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def solve(i,j):
            if dp[i][j] != 0:
                return dp[i][j]
            best = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + solve(ni, nj))

            dp[i][j] = best
            return best

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, solve(i, j))

        return ans
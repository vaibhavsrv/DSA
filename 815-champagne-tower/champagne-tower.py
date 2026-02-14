class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp=[0.0]*(query_row +2)
        dp[0] =float(poured)
        for i in range(query_row):
            for j in range(i,-1,-1):
                over = max((dp[j] - 1.0) / 2.0, 0.0)
                dp[j]=over
                dp[j+1]+=over
        return min(1.0,dp[query_glass])

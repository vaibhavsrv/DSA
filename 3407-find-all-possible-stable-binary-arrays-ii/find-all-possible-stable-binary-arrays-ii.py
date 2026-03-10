class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        dp0 = [[0] * (one+1) for _ in range(zero+1)]
        dp1 = [[0] * (one+1) for _ in range(zero+1)]

        for i in range(1,min(limit,zero)+1):
            dp0[i][0] = 1
        for j in range(1,min(limit,one)+1):
            dp1[0][j] = 1
        for k in range(1,zero + 1):
            for x in range(1,one+1):
                dp0[k][x] = dp0[k-1][x] + dp1[k-1][x]

                if k > limit:
                    dp0[k][x] -= dp1[k-limit-1][x]
                dp1[k][x] = dp1[k][x-1] + dp0[k][x-1]
                if x > limit:
                    dp1[k][x] -= dp0[k][x-limit-1]
        return (dp0[zero][one] + dp1[zero][one]) % MOD
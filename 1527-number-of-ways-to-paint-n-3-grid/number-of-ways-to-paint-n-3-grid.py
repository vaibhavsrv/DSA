class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9+7
        diff = 1
        same = 1

        for _ in range(1,n):
            A =(3*diff + 2*same) % MOD
            B =(2*diff + 2*same) % MOD
            diff,same = A,B
        return 6*(diff+same)%MOD
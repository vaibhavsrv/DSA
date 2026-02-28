class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9+7
        answer = 0
        a = 1
        b = 2
        for i in range(1,n+1):
            if i == b:
                a += 1
                b *= 2
            answer=((answer << a)+i)%MOD
        return answer
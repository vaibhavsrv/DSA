class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            count+=(ord(s[i])^i)&1
        return min(count,n-count)
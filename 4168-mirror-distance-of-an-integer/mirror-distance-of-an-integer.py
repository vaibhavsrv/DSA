class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse = int(str(n)[::-1])
        result = abs(n - reverse)
        return result
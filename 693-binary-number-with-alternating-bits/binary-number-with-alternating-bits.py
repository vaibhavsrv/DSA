class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        hello=bin(n)
        if len(hello) == 1:
            return True
        for i in range(1,len(hello)):
            if hello[i-1] == hello[i]:
                return False
        return True
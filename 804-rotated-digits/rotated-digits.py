class Solution:
    def isValid(self, n: int) -> bool:
        result = False

        while n > 0:
            digit = n % 10
            n //= 10

            if digit in (0,1,8):
                continue
            
            if digit in (2,5,6,9):
                result = True
            else:
                return False

        return result

    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            if self.isValid(i):
                count += 1

        return count
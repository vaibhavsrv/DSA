class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product = 1
        sums = 0
        i = n

        while i:
            digit = i % 10
            i //= 10

            product *= digit
            sums += digit

        return n % (product + sums) == 0
            
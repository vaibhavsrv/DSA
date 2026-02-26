class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        carry = False
        for i in s[:0:-1]:
            if i == '1' and not carry or i == '0' and carry:
                result += 2
                carry = True
            else:
                result += 1
        return result + int(carry)
class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        carry = False
        # the loop will be start from end->till it find 0, in reverse order
        for i in s[:0:-1]:
            if i == '1' and not carry or i == '0' and carry: # if this possible then add 2 to the result
                result += 2
                carry = True
            else:
                result += 1
        return result + int(carry)
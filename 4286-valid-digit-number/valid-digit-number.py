class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        string = str(n)
        if str(x) in string and str(x) != string[0]:
            return True
        return False
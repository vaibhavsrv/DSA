class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new = ""
        total = 0
        for ch in str(n):
            if ch != '0':
                new += ch
                total += int(ch)

        if new == "":
            return 0

        return int(new) * total
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""

        for ch in s:
            num += str(ord(ch) - ord("a") + 1)

        while k:
            count = 0

            for digit in num:
                count += int(digit)

            num = str(count)
            k -= 1

        return int(num)
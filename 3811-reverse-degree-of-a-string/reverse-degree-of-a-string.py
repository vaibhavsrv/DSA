class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            ch = s[i]
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                value = 26 - (ord(ch) - ord('a'))

                total += value * (i+1)

        return total
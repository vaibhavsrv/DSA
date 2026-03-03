class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n):
            invert = ""
            for c in s:
                if c == '0':
                    invert += '1'
                else:
                    invert += '0'
            s = s + "1" + invert[::-1]
        return s[k-1]
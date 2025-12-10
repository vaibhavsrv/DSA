class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s

        rows = [[] for _ in range(numRows)]
        i, d = 0, 1

        for char in s:
            rows[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d

        return ''.join(''.join(row) for row in rows)

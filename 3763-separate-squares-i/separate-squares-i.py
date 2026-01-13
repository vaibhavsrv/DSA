class Solution:
    def separateSquares(self, squares):
        low = 0.0
        high = 0.0

        for x, y, s in squares:
            high = max(high, y + s)

        for _ in range(100):
            mid = (low + high) / 2.0
            below = 0.0
            above = 0.0

            for x, y, s in squares:
                bottom = y
                top = y + s
                area = s * s

                if mid <= bottom:
                    above += area
                elif mid >= top:
                    below += area
                else:
                    below += (mid - bottom) * s
                    above += (top - mid) * s

            if below >= above:
                high = mid
            else:
                low = mid

        return high

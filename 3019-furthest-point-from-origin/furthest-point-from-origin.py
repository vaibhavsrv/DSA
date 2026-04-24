class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = right = dist = 0
        for c in moves:
            if c == 'L':
                left += 1
            elif c == 'R':
                right += 1
            else:
                dist += 1

        return abs(left - right) + dist
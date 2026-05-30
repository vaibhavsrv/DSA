from sortedcontainers import SortedList
from typing import List


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (4 * n)

    def update(self, node, start, end, position, value):
        if start == end:
            self.t[node] = value
            return
        mid = (start + end) // 2
        if position <= mid:
            self.update(2 * node, start, mid, position, value)
        else:
            self.update(2 * node + 1, mid + 1, end, position, value)
        self.t[node] = max(self.t[2 * node], self.t[2 * node + 1])

    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return self.t[node]
        mid = (start + end) // 2
        return max(
            self.query(2 * node, start, mid, left, right),
            self.query(2 * node + 1, mid + 1, end, left, right),
        )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        maxNUMBER = 50001
        seg = SegmentTree(maxNUMBER)
        obj = SortedList([0])
        result = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = obj.bisect_left(x) - 1
                prev = obj[idx]
                seg.update(1, 0, maxNUMBER - 1, x, x - prev)
                nxt_idx = idx + 1
                if nxt_idx < len(obj):
                    nxt = obj[nxt_idx]
                    seg.update(1, 0, maxNUMBER - 1, nxt, nxt - x)
                obj.add(x)
            else:
                x, sz = q[1], q[2]
                idx = obj.bisect_right(x) - 1
                last = obj[idx]
                partial = x - last
                best = seg.query(1, 0, maxNUMBER - 1, 0, x)
                best = max(best, partial)
                result.append(best >= sz)

        return result

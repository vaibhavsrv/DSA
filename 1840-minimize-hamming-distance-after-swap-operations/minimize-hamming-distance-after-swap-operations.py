class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = [x for x in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            findA = find(a)
            findB = find(b)

            if findA != findB:
                parent[findB] = findA

        for a,b in allowedSwaps:
            union(a,b)

        groups = {}

        for i in range(n):
            p = find(i)
            if p not in groups:
                groups[p] = []
            groups[p].append(i)

        answer = 0

        for group in groups.values():
            count = {}

            for i in group:
                val = source[i]
                if val not in count:
                    count[val] = 0
                count[val] += 1

            for i in group:
                val = target[i]
                if val in count and count[val] > 0:
                    count[val] -= 1
                else:
                    answer += 1

        return answer
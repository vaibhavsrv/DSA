class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        hashmap = {}
        for i in range(n):
            if arr[i] not in hashmap:
                hashmap[arr[i]] = []

            hashmap[arr[i]].append(i)

        queue = [0]
        visited = set([0])

        moves = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                i = queue.pop(0)

                if i == n - 1:
                    return moves

                neighbours = []

                neighbours += hashmap[arr[i]]

                neighbours.append(i+1)
                neighbours.append(i-1)

                for nextstep in neighbours:
                    if 0 <= nextstep < n and nextstep not in visited:
                        visited.add(nextstep)
                        queue.append(nextstep)

                hashmap[arr[i]] = []

            moves += 1                
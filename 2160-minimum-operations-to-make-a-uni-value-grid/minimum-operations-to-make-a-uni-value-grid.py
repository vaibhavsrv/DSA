class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        result = []

        for row in grid:
            for value in row:
                result.append(value)

        remainder = result[0] % x
        for value in result:
            if value % x != remainder:
                return -1

        result.sort()
        median = result[len(result) // 2]

        operations = 0
        for value in result:
            operations += abs(value - median) // x

        return operations



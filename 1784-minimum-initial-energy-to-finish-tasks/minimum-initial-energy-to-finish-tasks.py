class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: -(t[1] - t[0]))
        current = 0
        result  = 0
        for actual, minimum in tasks:
            if current < minimum:
                result  += (minimum - current)
                current  = minimum

            current -= actual
        return result
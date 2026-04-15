class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        shortest = n
        if target not in words:
            return -1
        for i in range(n):
            if words[i] == target:
                distance = abs(startIndex - i)
                shortest = min(shortest,min(distance,n - distance))
        return shortest
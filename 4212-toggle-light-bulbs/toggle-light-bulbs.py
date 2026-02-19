class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        from collections import Counter
        count = Counter(bulbs)
        seen = [bulb for bulb, val in count.items() if val%2!=0]
        return sorted(seen)
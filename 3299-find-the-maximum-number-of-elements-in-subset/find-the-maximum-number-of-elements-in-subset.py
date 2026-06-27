class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 0
        from collections import Counter

        count = Counter(nums)

        if count[1] > 0:
            ans = count[1] if count[1] % 2 == 1 else count[1] - 1

        for x in count:
            if x == 1:
                continue

            curr = x
            total = 0

            while count[curr] >= 2:
                total += 2
                curr = curr * curr

            if count[curr] >= 1:
                total += 1
            else:
                total -= 1
            ans = max(ans, total)

        return ans

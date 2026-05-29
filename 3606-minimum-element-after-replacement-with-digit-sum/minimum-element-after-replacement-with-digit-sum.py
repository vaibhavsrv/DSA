class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            total = 0
            for digit in str(num):
                total += int(digit)

            ans.append(total)

        return min(ans)
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, value in enumerate(nums):
            dgsum = 0
            while value > 0:
                dgsum += value % 10
                value //= 10

            if dgsum==i:
                return i

        return -1
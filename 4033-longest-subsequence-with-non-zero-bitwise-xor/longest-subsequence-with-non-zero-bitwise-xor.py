class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        tot = new = 0

        for n in nums:
            new |= n > 0
            tot ^= n

        return new * (len(nums) - (not tot))
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix = [0] * n
        suffix[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffix[i] = min(suffix[i+1],nums[i])

        prefix = nums[0]
        for i in range(n):
            prefix = max(prefix,nums[i])

            if prefix - suffix[i] <= k:
                return i
        return -1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            total += x
        left = 0
        for i in range(len(nums)):
            total -= nums[i]
            if left == total:
                return i
                break
            left += nums[i]
        return -1
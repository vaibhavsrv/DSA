class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currentsum = nums[0]
        for num in nums[1:]:
            currentsum = max(num,currentsum+num)
            maxsum = max(maxsum,currentsum)
        return maxsum
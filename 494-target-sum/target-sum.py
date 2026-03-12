class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i,current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0
            if (i,current_sum) in memo:
                return memo[(i,current_sum)]
            memo[(i,current_sum)] = dp(i+1,current_sum + nums[i]) + dp(i+1,current_sum - nums[i])
            return memo[(i,current_sum)]
        return dp(0,0)
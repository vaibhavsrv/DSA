class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # THE IS THE RECURSIVE CODE FOR THIS
        memo = {}
        def dp(i,current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0
            if (i,current_sum)in memo: # THIS LINE IS FOR MEMOIZATION
                return memo[(i,current_sum)] # RETURN THE MOMO
            memo[(i,current_sum)] = dp(i+1,current_sum + nums[i]) + dp(i+1,current_sum - nums[i]) # CALLING RECURSION HERE
            return memo[(i,current_sum)]
        return dp(0,0)# RECURSION BASE CASE
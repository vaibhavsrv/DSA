class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def robbery(i,dp:dict):
            if i == n:
                return 0
            if i == n-1:
                return nums[n-1]
            if i not in dp:
                rob = nums[i] + robbery(i+2,dp)
                skip = robbery(i+1,dp)

                dp[i] = max(rob,skip)
            return dp[i]
        return robbery(0,{})

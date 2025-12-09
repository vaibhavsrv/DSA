class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        '''def robbery(i,dp:dict):
            if i == n:
                return 0
            if i == n-1:
                return nums[n-1]
            if i not in dp:
                rob = nums[i] + robbery(i+2,dp)
                skip = robbery(i+1,dp)

                dp[i] = max(rob,skip)
            return dp[i]
        return robbery(0,{})'''
        if n <= 2:
            return max(nums)
        dp = [0]*n
        dp[0],dp[1] = nums[0],nums[1]
        dp[2]=nums[2]+dp[0]
        for i in range(3,n):
            dp[i]=max(dp[i-2],dp[i-3])+nums[i]
        return max(dp[-2:])

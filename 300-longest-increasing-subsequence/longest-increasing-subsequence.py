class Solution:
    def lengthOfLIS(self,nums):
        n = len(nums)
        '''memo = {}
        def dp(i,prev):
            if i == n:
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]
            skip = dp(i+1,prev)
            take = 0
            if nums[i] > prev:
                take = 1 + dp(i+1,nums[i])
            memo[(i,prev)] =  max(take,skip)
            return memo[(i,prev)]
        return dp(0,float('-inf'))''' 
        max_len = 1
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i]= max(dp[i],dp[j]+1)
                max_len = max(max_len,dp[i])
        return max_len
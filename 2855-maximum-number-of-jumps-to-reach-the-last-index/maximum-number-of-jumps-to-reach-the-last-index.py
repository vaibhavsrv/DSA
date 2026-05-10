class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i):
            if i == 0: return 0
            a = -inf
            for j in range(i):
                if abs(nums[j] - nums[i]) <= target:
                    a = max(a,1 + dfs(j))
            return a

        a = dfs(len(nums) - 1)
        return -1 if a < 0 else a
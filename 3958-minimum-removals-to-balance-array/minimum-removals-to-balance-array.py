class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_win = 0
        j = 0
        for i in range(n):
            while j < n and nums[j] <= k * nums[i]:
                j+=1
            max_win = max(max_win,j-i)
        return n - max_win
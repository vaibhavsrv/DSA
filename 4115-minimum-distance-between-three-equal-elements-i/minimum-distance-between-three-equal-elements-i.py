class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minDiff = float(inf)
        if len(nums) <= 2:
            return -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        dist = abs(i - j) + abs(j - k) + abs(k - i)
                        minDiff = min(minDiff,dist)
        return minDiff if minDiff != float(inf) else -1
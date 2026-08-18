class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] > threshold:
                count = 0

            elif count > 0 and nums[i] % 2 != nums[i-1] % 2:
                count += 1

            elif nums[i] % 2==0:
                count = 1

            else:
                count = 0
                
            ans = max(ans,count)

        return ans
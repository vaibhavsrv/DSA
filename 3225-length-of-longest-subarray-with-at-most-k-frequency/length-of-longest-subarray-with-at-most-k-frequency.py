class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        right = 0
        left = 0
        count = 0
        
        for right in range(len(nums)):
            if nums[right] in freq:
                freq[nums[right]] +=1
            else:
                freq[nums[right]] = 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            count= max(count,right - left+1)


        return count
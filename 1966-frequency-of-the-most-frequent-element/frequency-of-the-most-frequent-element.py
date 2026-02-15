class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        total=0
        i=0
        ans=0
        for j in range(len(nums)):
            total+=nums[j]
            while total+k<nums[j]*(j-i+1):
                total-=nums[i]
                i+=1
            ans=max(ans,(j-i+1))
        return ans
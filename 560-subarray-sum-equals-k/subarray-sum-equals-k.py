class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrayCount = 0 # initial count
        prefix_sum = 0 # going to use prefix sum approach

        freq = {0:1} #Initially we have key 0 which have value 1

        for i in nums:
            prefix_sum += i
            
            if prefix_sum - k in freq:
                subarrayCount += freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum,0) + 1

        return subarrayCount

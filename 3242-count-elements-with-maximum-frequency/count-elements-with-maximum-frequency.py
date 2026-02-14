class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        ans = 0
        for i in nums:
            freq[i] = freq.get(i,0)+1
        max_freq = max(freq.values())
        for count in freq.values():
            if count == max_freq:
                ans+=count
        return ans
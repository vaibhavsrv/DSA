class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}
        n = len(nums)

        for i in range(n-k+1):
            seen = set()   

            for j in range(i,i+k):
                seen.add(nums[j])

            for num in seen:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

        ans = -1

        for num in freq:
            if freq[num] == 1:
                ans = max(ans,num)

        return ans
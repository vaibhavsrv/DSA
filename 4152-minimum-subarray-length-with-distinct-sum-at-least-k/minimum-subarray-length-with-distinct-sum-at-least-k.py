class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        summ=0
        ans=float("inf")
        l=0
        for r in range(len(nums)):
            if freq[nums[r]]==0:
                summ+=nums[r]
            freq[nums[r]]+=1
            while summ>=k:
                ans=min(ans,(r-l)+1)
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    summ-=nums[l]

                l+=1
        return ans if ans!=float('inf') else -1
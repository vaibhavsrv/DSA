class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] +=1 
  
        bucket = [[] for _ in range(len(nums)+ 1)]

        for num in map:
            bucket[map[num]].append(num)

        ans = []

        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        count = 0
        
        for i in range(len(cost)):
            if i % 3 != 2:
                count += cost[i]

        return count
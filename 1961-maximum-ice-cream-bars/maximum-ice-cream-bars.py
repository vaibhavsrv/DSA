class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()

        for i in range(len(costs)):
            if costs[i] <= coins:
                count += 1
                coins -= costs[i]
                i+= 1

        return count
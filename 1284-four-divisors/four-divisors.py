class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            count = 0
            div_sum = 0
            for j in range(1,int(math.sqrt(i))+1):
                if i%j == 0:
                    k=i//j
                    if k == j:
                        count += 1
                        div_sum += (j)
                    else:
                        count += 2
                        div_sum += (j+k)
                if count>4:
                    break
            if count == 4:
                ans += div_sum
        return ans
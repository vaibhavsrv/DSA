class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # ITS A BRUTE FORCE APPROACH TO GET THE SUBARRAY SUM DIV BY K
        '''n = len(nums)
        count = 0 MAINTAIN A COUNT 
        for i in range(n):
            summ = 0 INITIALIZE THE SUM INITIALLY BE ZERO
            for j in range(i,n):
                summ += nums[j] THEN START ADDING NUMS[J]
                if (summ % k) == 0: IF CONDITION IS GETTING SATISFIED INCREASE THE COUNT 
                    count += 1
        return count'''
        # THE OPTIMAL WILL BE SOLVED USING PREFIX SUM
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1 # the count initially be 1
        prefix = 0
        answer = 0

        for i in nums:
            prefix += i # add every element of nums in prefix
            check = prefix % k # here is the check var 
            # IF YESSS THEN
            answer += count[check] # add the count of check in the answer
            count[check] += 1 #increase the count
        return answer

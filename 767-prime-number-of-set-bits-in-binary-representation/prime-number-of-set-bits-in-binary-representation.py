class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        '''a,b=bin(left),bin(right)'''
        result = 0
        prime_nums ={2,3,5,7,11,13,17,19}
        for i in range(left,right+1):
            bits = bin(i).count('1')
            if bits in prime_nums:
                result+=1
        return result
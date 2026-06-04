class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for n in range(num1,num2+1):
            digits = list(map(int,str(n)))

            i = 1
            while i < len(digits)-1:
                if digits[i] > digits[i-1] and digits[i] > digits[i+1]:
                    waviness += 1

                elif digits[i] < digits[i-1] and digits[i] < digits[i+1]:
                    waviness += 1

                i+=1

        return waviness
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxZero = 0
        maxOne = 0
        count0 = 0
        count1 = 0
        for c in s:
            if c == '1':
                count1 += 1
                count0 = 0
            else:
                count0 += 1
                count1 = 0

            maxZero = max(maxZero,count0)
            maxOne = max(maxOne,count1)
        if maxOne>maxZero:
            return True
        else:
            return False
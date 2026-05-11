class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        SINGLEdigitSum = 0
        DOUBLEdigitSum = 0

        for i in nums:
            if int(i) < 10:
                SINGLEdigitSum += i
            else:
                DOUBLEdigitSum += i

        if SINGLEdigitSum != DOUBLEdigitSum:
            return True

        return False
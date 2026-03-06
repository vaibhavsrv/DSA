class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segment = 0
        for i in range(len(s)):
            if s[i] == '1' and (i==0 or s[i-1] =='0'):
                segment += 1
        if segment == 1:
            return True
        else:
            return False
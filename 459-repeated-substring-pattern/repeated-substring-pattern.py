class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # return s in (s+s)[1:-1]

        n = len(s)

        for i in range(1,n//2+1):
            if n % i == 0:
                pattern = s[:i]

            if pattern * (n // i) == s:
                return True
            
        return False

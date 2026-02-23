class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        codes = 2**k
        seen = set()
        for i in range(k,n+1):
            substring = s[i-k:i]
            if substring not in seen:
                seen.add(substring)
                codes -= 1
            if codes == 0:
                return True
        return False
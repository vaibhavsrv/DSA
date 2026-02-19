class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev = 0
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                prev = count
                count = 1
            if count <= prev:
                result += 1
        return result
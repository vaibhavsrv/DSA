class Solution:
    def longestPalindrome(self, s: str) -> str:
        i , j = 0 , len(s)
        while j > 0:
            while i + j <= len(s):
                if s[i:i+j] == s[i:i+j][::-1]:
                    return s[i:i+j]

                i += 1
            i = 0
            j -= 1

        return s
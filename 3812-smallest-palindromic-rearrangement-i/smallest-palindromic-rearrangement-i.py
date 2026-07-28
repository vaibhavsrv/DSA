class Solution:
    def smallestPalindrome(self, s: str) -> str:
        size = len(s)
        firstHalf: str = s[0: size // 2]
        mid: str = ""
        if size % 2 == 1:
            mid = s[size // 2]
        return "".join(sorted(firstHalf)) + mid + "".join(sorted(firstHalf, reverse=True))
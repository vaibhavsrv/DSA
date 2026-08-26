class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        left = 0
        count = 0
        minL = float('inf')
        for right in range(len(s)):
            if s[right] == '1':
                count += 1
            while count == k:
                sub = s[left:right+1]
                    
                if len(sub) < minL or (len(sub) == minL and sub < ans):
                    ans = sub
                    minL = len(sub)
                if s[left] == '1':
                    count -= 1

                left+=1
        return ans

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPalindrome(i,j):
            while i<j:
                if s[i] != s[j]:
                    return False
                i+= 1
                j-= 1
            return True
        def dp(i,current):
            if i == len(s): # BASE CASE
                result.append(current[:])
                return
            for j in range(i,len(s)):
                if isPalindrome(i,j):
                    current.append(s[i:j+1])
                    dp(j+1,current)
                    current.pop()
        dp(0,[])
        return result
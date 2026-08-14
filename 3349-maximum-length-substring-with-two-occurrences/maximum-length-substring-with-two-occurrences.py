class Solution:
    def maximumLengthSubstring(self, s: str) -> int:       
        new={}
        low = 0
        ans = 0
        for high in range(len(s)):
            new[s[high]] = new.get(s[high],0)+1

            while new[s[high]] > 2:
                new[s[low]] -=1
                low +=1

            ans = max(ans,high - low +1)

        return ans
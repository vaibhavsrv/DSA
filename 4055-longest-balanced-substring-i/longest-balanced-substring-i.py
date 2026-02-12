class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        ans = 0
        for i in range(n):
            freq=[0] * 26
            distinct = 0
            maxfreq = 0
            for j in range(i,n):
                index=ord(s[j])-ord('a')
                if freq[index] == 0:
                    distinct+=1
                freq[index]+=1
                maxfreq = max(maxfreq,freq[index])
                length = j-i+1
                if length == distinct*maxfreq:
                    ans=max(ans,length)
        return ans
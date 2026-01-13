class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        max_length = 0
        dp = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                ans = word[:i] + word[i+1:]
                if ans in dp:
                    dp[word] = max(dp[word],dp[ans]+1)
            max_length = max(max_length,dp[word])
        return max_length
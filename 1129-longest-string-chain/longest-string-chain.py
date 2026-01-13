class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        max_chain=0
        dp={}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i]+word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word],dp[prev]+1)
                max_chain = max(max_chain,dp[word])
        return max_chain
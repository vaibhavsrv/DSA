class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        memo={}
        def dp(word):
            if word not in word_set:
                return 0
            if word in memo:
                return memo[word]
            max_chain = 1
            for i in range(len(word)):
                prev = word[:i]+word[i+1:]
                max_chain = max(max_chain,1+dp(prev))
            memo[word] = max_chain
            return max_chain
        return max(dp(word) for word in words)
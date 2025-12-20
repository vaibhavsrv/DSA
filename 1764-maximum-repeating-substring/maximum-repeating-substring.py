class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        max_count = 0
        n1 = len(sequence)
        n2 = len(word)

        for i in range(n1):
            while i<=n1-n2 and sequence[i:i+n2]==word:
                count+=1
                i+=n2
            max_count=max(max_count,count)
            count = 0
            
        return max_count
                
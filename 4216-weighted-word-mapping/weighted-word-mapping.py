class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            total_weights = 0
            for ch in word:
                total_weights += weights[ord(ch) - ord('a')]
            modulo = total_weights % 26
            result.append(chr(ord('z')-modulo))
        return "".join(result)
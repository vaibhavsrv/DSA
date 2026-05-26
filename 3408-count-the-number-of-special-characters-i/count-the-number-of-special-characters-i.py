class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_count = set()
        upper_count = set()

        for ch in word:
            if ch.islower():
                lower_count.add(ch)
            else:
                upper_count.add(ch)
        
        count  = 0

        for ch in lower_count:
            if ch.upper() in upper_count:
                count += 1

        return count

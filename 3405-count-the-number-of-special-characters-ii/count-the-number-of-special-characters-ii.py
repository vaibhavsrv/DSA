class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}
        invalid = set()

        for i,ch in enumerate(word):
            l = ch.lower()

            if ch.islower():
                lower[l] = i

                if l in upper:
                    invalid.add(l)
            else:
                if l not in upper:
                    upper[l] = i

        count = 0
        for l in lower:
            if l in upper and l not in invalid:
                count += 1

        return count
            
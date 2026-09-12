class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = []

        for ch in s:
            if ch in 'aeiouAEIOU':
                vowel.append(ch)
        vowel = vowel[::-1]

        ans = ""
        j = 0

        for ch in s:
            if ch in 'aeiouAEIOU':
                ans += vowel[j]

                j+=1

            else:
                ans += ch
        return ans
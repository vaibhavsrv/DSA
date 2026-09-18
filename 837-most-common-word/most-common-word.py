class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        freq = {}
        banned = set(banned)

        paragraph = paragraph.lower()

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch," ")

        for word in paragraph.split():
            if word not in banned:
                freq[word] = freq.get(word,0)+1
        
        ans = ""

        for word in freq:
            if ans == "" or freq[word] > freq[ans]:
                ans = word

        return ans
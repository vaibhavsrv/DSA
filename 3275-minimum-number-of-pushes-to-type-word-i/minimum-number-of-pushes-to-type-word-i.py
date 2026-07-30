class Solution:
    def minimumPushes(self, word: str) -> int:
        click = 0

        for i in range(len(word)):
            click += (i // 8) + 1

        return click
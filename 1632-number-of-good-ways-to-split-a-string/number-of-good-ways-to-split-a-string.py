class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        seenLeft , leftCount = set(), []
        for idx , ch in enumerate(s):
            seenLeft.add(ch)
            leftCount.append(len(seenLeft))

        seenRight = set()
        for idx in range(len(s)-1,0,-1):
            seenRight.add(s[idx])
            if len(seenRight) == leftCount[idx-1]:
                ans += 1

        return ans

        
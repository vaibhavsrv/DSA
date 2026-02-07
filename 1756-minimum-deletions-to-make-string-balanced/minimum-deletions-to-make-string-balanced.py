class Solution:
    def minimumDeletions(self, s: str) -> int:
        countB = 0
        n=len(s)
        deletion=0
        for i in range(n):
            if s[i] == 'b':
                countB+=1
            else:
                deletion = min(deletion+1,countB)
        return deletion

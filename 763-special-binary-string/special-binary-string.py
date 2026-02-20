class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        result = []
        for j in range(len(s)):
            if s[j] == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                special = self.makeLargestSpecial(s[i+1:j])
                result.append('1' + special + '0')
                i = j + 1
        result.sort(reverse=True)
        return ''.join(result)
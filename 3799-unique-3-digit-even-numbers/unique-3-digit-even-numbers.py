class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        num = set()

        for i,j,k in permutations(digits,3):
            if i != 0 and k % 2 == 0:
                num.add((i,j,k,))

        return len(num)
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp = []
        for num in arr:
            temp.append((bin(num).count('1'),num))
        temp.sort()
        answer = []
        for item in temp:
            answer.append(item[1])
        return answer
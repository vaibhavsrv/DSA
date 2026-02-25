class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Brute Force solution of O(nlogn), it works because the constraints is only 500
        temp = []
        for num in arr:
            temp.append((bin(num).count('1'),num))
        temp.sort()
        answer = []
        for item in temp:
            answer.append(item[1])
        return answer

        #Optimal can be something like we can sort with key pair and use lambda function
        return sorted(arr,key=lambda x:bin(x).count('1'))
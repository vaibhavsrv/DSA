class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        appleSum = sum(apple)
        # print("totalapples",appleSum)
        
        capacity.sort(reverse=True)
        for i in range(len(capacity)):
            if appleSum > capacity[i]:
                appleSum -= capacity[i]
            else:
                return i+1  
        return len(capacity)        
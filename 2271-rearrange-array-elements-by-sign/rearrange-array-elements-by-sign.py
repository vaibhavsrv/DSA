class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveElement = [] # Created two list to store +ve values
        negativeElement = [] # For -ve values
        result = [] # Merged both of them

        for i in nums:
            if i > 0:
                positiveElement.append(i)
            else:
                negativeElement.append(i)

        for i in range(len(positiveElement)):
            result.append(positiveElement[i])
            result.append(negativeElement[i])
            
        return result
        
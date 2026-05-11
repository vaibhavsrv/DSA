class Solution:
    def countEven(self, num: int) -> int:
        count = 0 # initially the count will be zero
        #itereting through each i to num+1
        for i in range(1,num+1):
            SUM = 0 # its the digit sum initially 0
            for d in str(i):
                SUM += int(d) # added the number

            if SUM % 2 == 0: # check for even
                count += 1 # if yes then count + 1


        return count

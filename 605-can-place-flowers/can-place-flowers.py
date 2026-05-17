class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 1:
                i += 2

            elif i == len(flowerbed)-1 or flowerbed[i+1] == 0:
                n -= 1
                i += 2

            else:
                i += 3

        return n <= 0            

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        canPlant = streak = 0
        for num in [0] + flowerbed + [0]:
            if num == 1:
                streak = 0
            else:
                streak += 1
                if streak == 3:
                    canPlant += 1
                    streak = 1
        return canPlant >= n
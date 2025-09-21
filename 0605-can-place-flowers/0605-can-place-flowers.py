class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        arr = [0] + flowerbed + [0]
        canPlant = streak = 0
        for num in arr:
            if num == 1:
                streak = 0
            else:
                streak += 1
                if streak == 3:
                    streak = 1
                    canPlant += 1
        return canPlant >= n
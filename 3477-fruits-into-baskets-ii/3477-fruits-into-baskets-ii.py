class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = len(fruits)
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets[i] = 0
                    unplaced -= 1
                    break
        return unplaced
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = Counter(hand)
        for y in sorted(count):
            while count[y] > 0:
                for k in range(y, y + W):
                    count[k] -= 1
                    if count[k] < 0:
                        return False
        return True
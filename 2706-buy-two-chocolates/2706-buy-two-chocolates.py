class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min = secondMin = float('inf')
        for p in prices:
            if p <= min:
                min, secondMin = p, min
            elif p < secondMin:
                secondMin = p
        return money - min - secondMin if money >= min + secondMin else money
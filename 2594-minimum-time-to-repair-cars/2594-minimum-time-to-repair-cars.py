class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, max(ranks) * (cars**2)
        while l <= r:
            m = (l + r)//2
            if not self.canRepairKCars(ranks, cars, m):
                l = m + 1
            elif not self.canRepairKCars(ranks, cars, m - 1):
                return m
            else:
                r = m - 1

    def canRepairKCars(self, ranks, k, minutes):
        return sum(int((minutes//r)**0.5) for r in ranks) >= k
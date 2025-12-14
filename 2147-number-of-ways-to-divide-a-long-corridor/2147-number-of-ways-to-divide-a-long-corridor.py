class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seatCount = corridor.count('S')
        if seatCount == 0 or seatCount % 2 == 1: return 0
        ans = 1
        plants = seats = 0
        for ch in corridor:
            if ch == 'P':
                if seats == 2:
                    plants += 1
            else:
                seats += 1
                if seats == 3:
                    ans *= (plants + 1)
                    seats, plants = 1, 0
        return ans % (10**9 + 7)
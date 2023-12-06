class Solution:
    def totalMoney(self, n: int) -> int:
        perWeek = (7+1)*7//2
        weekCount = n//7
        remainDays = n % 7
        remain = ((weekCount + 1) + (weekCount + remainDays))*remainDays//2
        return perWeek*weekCount + 7*weekCount*(weekCount - 1)//2 + remain
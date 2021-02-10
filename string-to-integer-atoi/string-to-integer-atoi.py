class Solution:
    def myAtoi(self, s: str) -> int:
        num, sign, i = 0, 1, 0
        minInt, maxInt = -2**31, 2**31 - 1
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in '-+':
            if s[i] == '-': sign = -1
            i += 1
        while i < len(s) and s[i].isdigit():
            if num > maxInt//10 or (num == maxInt//10 and int(s[i]) > 7):
                return maxInt if sign == 1 else minInt
            num = num * 10 + int(s[i])
            i += 1
        return num * sign
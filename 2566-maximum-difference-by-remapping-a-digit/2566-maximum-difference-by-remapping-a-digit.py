class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        minNum = s.replace(s[0], '0')
        maxNum = s
        for ch in s:
            if ch != '9':
                maxNum = s.replace(ch, '9')
                break
        return int(maxNum) - int(minNum)
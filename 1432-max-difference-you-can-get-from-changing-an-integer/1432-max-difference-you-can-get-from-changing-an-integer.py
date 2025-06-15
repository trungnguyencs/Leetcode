class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        minNum, maxNum = s, s
        for ch in maxNum:
            if ch != '9':
                maxNum = maxNum.replace(ch, '9')
                break
        if minNum[0] != '1':
            minNum = minNum.replace(minNum[0], '1')
        else:
            for i in range(1, len(minNum)):
                if minNum[i] not in '01':
                    minNum = minNum.replace(minNum[i], '0')
                    break
        return int(maxNum) - int(minNum)
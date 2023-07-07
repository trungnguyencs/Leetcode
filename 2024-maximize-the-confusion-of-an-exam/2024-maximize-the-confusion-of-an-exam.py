class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = lt = lf = 0
        trueRemain = falseRemain = k
        for r, val in enumerate(answerKey):
            if val == 'F':
                falseRemain -= 1
                while falseRemain < 0:
                    if answerKey[lt] == 'F':
                        falseRemain += 1
                    lt += 1
            else:
                trueRemain -= 1
                while trueRemain < 0:
                    if answerKey[lf] == 'T':
                        trueRemain += 1
                    lf += 1
            ans = max(ans, r - lt + 1, r - lf + 1)
        return ans
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # [s, e, val] == [s, length-1, val] + [e+1, length-1, -val]
        ans = [0]*length
        for s, e, val in updates:
            ans[s] += val
            if e < length - 1: ans[e + 1] -= val
        carry = 0
        for i in range(len(ans)):
            ans[i] += carry
            carry = ans[i]
        return ans
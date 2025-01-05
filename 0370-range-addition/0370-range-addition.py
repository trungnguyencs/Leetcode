class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        #add x to range [l, r] is equivalent to add x to range [l, n-1] plus add -x to range [r+1, n-1]
        ans = [0]*length
        for l, r, val in updates:
            ans[l] += val
            if r < length - 1:
                ans[r+1] -= val
        for i in range(1, length):
            ans[i] += ans[i-1]
        return ans
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # a ^ b = c => b = c ^ a
        arr = [pref[0]]*len(pref)
        for i in range(1, len(arr)):
            arr[i] = pref[i] ^ pref[i-1]
        return arr   
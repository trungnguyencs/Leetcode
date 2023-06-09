class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            m = (l + r)//2
            if ord(letters[m]) <= ord(target):
                l = m + 1
            elif m > 0 and ord(letters[m-1]) <= ord(target):
                return letters[m]
            else:
                r = m - 1
        return letters[0]
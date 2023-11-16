class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # brute force solution: convert to number and find a number between [0, 2**n - 1] not in the input set
        # smart solution: ith bit of ans is the opposite of ith bit of ith string -> ans differs from each string by at least 1 bit
        ans = []
        for i, s in enumerate(nums):
            ans.append('1' if s[i] == '0' else '0')
        return ''.join(ans)
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        cur = num[0]
        count = 0
        for ch in num:
            if ch == cur:
                count += 1
                if count == 3 and (ans == "" or ord(ch) > ord(ans[0])):
                    ans = ch*3
            else:
                cur = ch
                count = 1
        return ans
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        dic = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        ans = []
        for c, biz, active in zip(code, businessLine, isActive):
            if active and biz in dic and self.isCodeValid(c):
                ans.append((c, biz))
        ans.sort(key=lambda x: (dic[x[1]], x[0]))
        return [c for c, _ in ans]

    def isCodeValid(self, code):
        return len(code) > 0 and all(ch.isalnum() or ch == '_' for ch in code)
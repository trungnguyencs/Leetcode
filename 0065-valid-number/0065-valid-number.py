import re
class Solution:
    def isNumber(self, s: str) -> bool:
        subpattern = f"[+-]?(([0-9]+\.?[0-9]*)|([0-9]*\.?[0-9]+))"
        pattern = f"^{subpattern}([eE][+-]?[0-9]+)?$"
        return bool(re.match(pattern, s.strip()))
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        #subpattern handles everything before [eE], "1." and ".1" are both True, but "." is False
        subpattern = f"[+-]?(([0-9]+\.?[0-9]*)|([0-9]*\.?[0-9]+))"
        pattern = f"^{subpattern}([eE][+-]?[0-9]+)?$"
        return bool(re.match(pattern, s.strip()))
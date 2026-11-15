class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = list(s)
        chars_t = list(t)
        chars_s.sort()
        chars_t.sort()
        return chars_s == chars_t
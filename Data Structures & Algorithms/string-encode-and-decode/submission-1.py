class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += "||" + string
        return result

    def decode(self, s: str) -> List[str]:
        return s.split("||")[1:]
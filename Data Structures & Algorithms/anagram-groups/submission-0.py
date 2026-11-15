class Solution:
    def isAnagram(self, value1: str, value2: str) -> bool:
        if len(value1) != value2:
            return False
        count = [0] * 26
        for index in range(len(value1)):
            count[ord(value1[index])-ord('a')] -=1
            count[ord(value2[index])-ord('a')] +=1
        return all(x == 0 for x in count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_string_dict: dict[str, list[str]] = {}

        for string in strs:
            sorted_string_dict.setdefault(''.join(sorted(string)), []).append(string)
        
        return list(sorted_string_dict.values())
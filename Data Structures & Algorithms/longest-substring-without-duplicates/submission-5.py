class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxP = pointer = min_pointer = 0
        dictionary = {}
        while pointer < len(s):
            curr_element = s[pointer]
            if curr_element in dictionary:
                min_pointer = max(min_pointer, dictionary[curr_element]+1)
            dictionary[curr_element] = pointer
            maxP = max(maxP, pointer - min_pointer+1)
            pointer +=1
        return maxP
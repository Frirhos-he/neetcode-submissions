class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        left, right = 0 , 0
        max_p = 0
        while right < len(s):
            curr_element = s[right]

            if curr_element not in unique_chars:
                unique_chars.add(curr_element)
            else:
                while s[left] != curr_element:
                    unique_chars.remove(s[left])
                    left+=1
                left+=1
            max_p = max(max_p, right - left + 1)
            right += 1
        return max_p


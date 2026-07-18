class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        if n == 0 or n == 1:
            return n


        longest_substring = 0
        char_counter = {}

        start_index = 0
        end_index = 0
        while end_index < n:
            char = s[end_index]
            if not char in char_counter:
                char_counter[char] = True
                longest_substring = max(end_index - start_index, longest_substring)
                end_index += 1
            else:
                del char_counter[s[start_index]]
                start_index += 1
        return longest_substring + 1
            


        


        
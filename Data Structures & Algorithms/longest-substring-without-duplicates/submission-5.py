class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        right = 0
        seen = set()
        longest = 0
        length = 0

        for left, char in enumerate(s):

            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                length += 1
                right += 1
            longest = max(length, longest)
            seen.remove(char)
            length -= 1

        return longest
            


        
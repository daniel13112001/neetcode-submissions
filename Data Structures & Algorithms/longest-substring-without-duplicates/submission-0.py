
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        longestSeen = 0

        for idx, char in enumerate(s):
            j = idx
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            longestSeen = max(longestSeen, len(seen))
            seen.clear()
        return longestSeen


        
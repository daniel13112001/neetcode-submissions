class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest = 0
        cur = 0
        seen = set()

        for c in s:
            while c in seen:
                seen.remove(s[l])
                l += 1
                cur -= 1

            seen.add(c)
            cur += 1
            longest = max(cur, longest)


        return longest





        
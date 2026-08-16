class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_char = [0] * 26
        t_char = [0] * 26

        for c in s:
            s_char[ord(c) - ord('a')] += 1

        for c in t:
            t_char[ord(c) - ord('a')] += 1

        return s_char == t_char
        
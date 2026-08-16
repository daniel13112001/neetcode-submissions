class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        longest = 0
        counts = [0] * 26

        for r, c in enumerate(s):
            counts[ord(c)-ord('A')] += 1
            while sum(counts) - max(counts) > k:
                counts[ord(s[l])-ord('A')] -= 1
                l += 1
            longest = max(longest, r-l+1)

        return longest
      
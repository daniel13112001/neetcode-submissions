class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        longest = 0
        charCounts = [0] * 26


        for right in range(len(s)):

            charCounts[ord(s[right])-ord('A')] += 1

            while left < len(s) and ((right-left+1) - max(charCounts)) > k:
                charCounts[ord(s[left])-ord('A')] -= 1
                left += 1
            
            longest = max(longest, (right-left+1))


        return longest
        
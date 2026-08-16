class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        left = 0
        charCounts = [0] * 26
        longest = 0


        for right, char in enumerate(s):

            charCounts[ord(char)-ord('A')] += 1

            while (right-left+1) - max(charCounts) > k:
                charCounts[ord(s[left])-ord('A')] -= 1
                left += 1
            longest = max(longest, (right-left)+1)
            
        

        return longest
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1CharCount = [0] * 26

        for char in s1:
            s1CharCount[ord(char)-ord('a')] += 1

        s2SubCount = [0] * 26

        left = 0

        for right in range(len(s2)):

            s2SubCount[ord(s2[right])-ord('a')] += 1

            if (right - left + 1) == len(s1):
                if s2SubCount == s1CharCount:
                    return True
                s2SubCount[ord(s2[left])-ord('a')] -= 1
                left += 1
            
        return False



        
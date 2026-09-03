class Solution:
    def countSubstrings(self, t: str) -> int:

        # Generate all substrings 
        # Check if it is a palindrome after 


        # racccar


        def expand(left, right):

            count = 0

            while left >= 0 and right < len(t) and t[left] == t[right]:
                count += 1
                left -= 1
                right += 1

            return count


        c = 0
        
        for i in range(len(t)):
            c += expand(i, i)
            c += expand(i, i+1)
        return c




        
        
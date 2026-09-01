class Solution:
    def longestPalindrome(self, s: str) -> str:

        lstr = ""


        def expandOutward(left, right):

            while left >= 0 and right < len(s) and left <= right:
                if s[left] != s[right]:
                    break

                left -= 1
                right += 1


            return s[left+1:right]
            

        for i in range(len(s)):

            odd = expandOutward(i,i)
            even = expandOutward(i,i+1)
            c = ""

            if len(odd) > len(even):
                c = odd 
            else:
                c = even 
            
            if len(c) > len(lstr):
                lstr = c


        return lstr





    
        
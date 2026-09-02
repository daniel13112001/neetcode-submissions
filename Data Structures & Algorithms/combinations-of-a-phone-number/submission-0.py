class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digitMap = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        res = []
        path = []


        def backtrack(i):

            if len(path) == len(digits):
                res.append("".join(path))
                return 
            if i >= len(digits):
                return 

            j = digits[i]
            letters = digitMap[int(j)]
            print(letters)

            for letter in letters:
                path.append(letter)
                backtrack(i+1)
                path.pop()

  
        backtrack(0)
        return res
        
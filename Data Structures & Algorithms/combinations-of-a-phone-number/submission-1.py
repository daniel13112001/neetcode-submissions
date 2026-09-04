class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        dmap = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        res = []
        path = []

        def backtrack(i): # i is the index of the current digit.
            
            if i >= len(digits):
                res.append(path[:])
                print(path[:])
                return 

            letters = dmap[int(digits[i])]

            for letter in letters:
                path.append(letter)
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return ["".join(r) for r in res]
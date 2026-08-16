class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = []
        path = []

        def findCombination(i, remaining):
            
            if remaining == 0:
                ans.append(path[:])
                print(path[:])
                return

            if i == len(candidates):
                return 
                
            if remaining < 0:
                return 

            # Choose index i
            path.append(candidates[i])
            findCombination(i+1, remaining-candidates[i])
            path.pop()


            # Skip index i and all copies of candidates[i]
            while i < len(candidates) -1 and candidates[i+1] == candidates[i]:
                i += 1
            findCombination(i+1, remaining)

        
        findCombination(0, target)

        return ans
        
        
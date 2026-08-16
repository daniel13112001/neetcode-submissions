class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        self.allPermutations(nums, 0, len(nums)-1, ans)
        return ans



    def allPermutations(self, nums, start, stop, sol):

        if start >= stop:
            sol.append(nums[:])
            return sol

        for i in range(start, stop+1):
            self.swap(nums, start, i)
            self.allPermutations(nums, start+1, len(nums)-1, sol)
            self.swap(nums, start, i)

        return sol

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]




        
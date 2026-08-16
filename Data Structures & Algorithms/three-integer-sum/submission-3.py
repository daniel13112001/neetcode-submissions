class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        sol = []
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            start = idx + 1
            end = len(nums) - 1
            target = -num

            while start < end:
                x = nums[start]
                y = nums[end]
                print(target,x,y)
                if x + y == target:
                    sol.append([num, x, y])
                    # TODO Advance each to next distinct
                    while start < end and nums[start] == x:
                        start += 1
                    while start < end and nums[end] == y:
                        end -= 1
                
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
        return sol
        
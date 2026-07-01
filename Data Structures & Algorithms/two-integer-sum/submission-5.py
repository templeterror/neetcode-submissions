class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val : index

        for index, value in enumerate(nums):
            complement = target - value # calculate diff

            if complement in seen:
                return [seen[complement], index]

            seen[value] = index # add new value and iterate loop again
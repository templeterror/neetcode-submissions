class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        work = {}
        for i in range(len(nums)):
            element = nums[i]
            complement = target - element
            if complement in work:
                return [work[complement], i]
            else :
                work[element] = i
        return None

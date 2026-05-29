class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index, value in enumerate(nums):
            complement = target - value

            for index1, value1 in enumerate(nums):
                if complement == value1 and index1!=index:
                    return [index,index1]

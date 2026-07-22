class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        S = {}

        for i, n in enumerate(nums):
            com = target - n
            if n in S:
                return [S[n], i]
            S[com] = i
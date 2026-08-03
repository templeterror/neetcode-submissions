class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()
        
        if (len(nums) < 3):
            return [list(i) for i in res]

        for i in range(0, len(nums) - 2, 1):
            l, r = i+1, len(nums) -1

            while l<r:
                if (nums[i] + nums[r] + nums[l]) == 0:
                    tmp = [nums[i], nums[l], nums[r]]
                    res.add(tuple(tmp))
                    l+=1
                    r-=1
                elif (nums[i] + nums[r] + nums[l]) < 0:
                    l+=1
                else:
                    r-=1

        return [list(i) for i in res]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #put length of nums to n variable
        n = len(nums)

        #intialize empty arrays and assign size to n
        pref = [0] * n
        suff = [0] * n
        res = [0] * n

        # set base case
        pref[0] = 1
        suff[n-1] = 1

        # populate pref
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #empty dict to put nums into
        count = {}

        #empty lists of lists for bucket sort
        freq = [[] for i in range(len(nums)+ 1)]

        #loop to populate dict, key = numbers, values = frequencies
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        # populate freq, indeces = frequencies = v, values = numbers = key
        for key, v in count.items():
            freq[v].append(key)
        
        #output list
        res = []

        #figure out top freqs from end of the freq array
        for i in range(len(freq)-1, 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res
                
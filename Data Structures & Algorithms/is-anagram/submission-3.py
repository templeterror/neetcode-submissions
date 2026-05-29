class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for i in range (len(s)):
            element = s[i]
            if element in dict1:
                dict1[element] += 1
            else:
                dict1[element] = 1
        
        dict2 = {}
        for i in range (len(t)):
            element = t[i]
            if element in dict2:
                dict2[element] += 1
            else:
                dict2[element] = 1

        return dict1 == dict2
        
            

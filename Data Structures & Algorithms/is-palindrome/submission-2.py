class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #empty list to take input strings elements:numbers and letters only
        clean =[]
        
        #loop to populate clean
        for ch in s:
            if ch.isalnum(): #boolean method that returns true if element is number/letter
                clean.append(ch)
        
        s = "".join(clean).lower() #method to create a new string from list elements, lowercase cast
        
        n = len(s)
        i = 0
        j = n-1
        p = (n-1)//2
        k = 0

        while k<=p:
            if s[i] == s[j]:
                i+=1
                j-=1
                k+=1
            else:
                return False
        return True
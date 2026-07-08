class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        S = {}
        T = {}

        for i in s:
            if i in S:
                S[i] = S.get(i, 0) + 1
            else:
                S[i] = 1

        for j in t:
            if j in T:
                T[j] = T.get(j, 0) + 1
            else:
                T[j] = 1

        if S == T :
            return True
        else:
            return False
        



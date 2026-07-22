class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        S = {}
        T = {}

        for i in s:
            S[i] = 1 + S.get(i,0)

        for j in t:
            T[j] = 1 + T.get(j, 0)

        if S == T:
            return True

        return False
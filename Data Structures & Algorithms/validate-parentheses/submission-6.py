class Solution:
    def isValid(self, s: str) -> bool:
        
        stik = []

        for i in s:
            if i not in "}])":
                stik.append(i)
            if i in "}])":
                if not stik:
                    return False
                if ((i == "}" and stik.pop() == "{") or
                    (i == "]" and stik.pop() == "[") or
                    (i == ")" and stik.pop() == "(")):
                     continue
                else:
                    return False
                
        return not stik
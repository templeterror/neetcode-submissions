class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p = 0
        q = len(s) - 1

        while p < q:
            if s[p].isalnum() and s[q].isalnum():
                if s[p] != s[q]:
                    return False
                p += 1
                q -= 1
            elif not s[p].isalnum():
                p += 1
            else:
                q -= 1

        return True
            
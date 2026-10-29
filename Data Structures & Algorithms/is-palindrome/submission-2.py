class Solution:
    def isalphanum(self, c):
        return ord('A') <= ord(c) <=ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord ('9')
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            if not self.isalphanum(s[i]):
                i+=1
            elif not self.isalphanum(s[j]):
                j-=1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i+=1
                j-=1
        return True
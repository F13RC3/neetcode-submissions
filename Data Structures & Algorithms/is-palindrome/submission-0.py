class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(filter(str.isalnum, s)).lower()
        return cleaned_s == cleaned_s[::-1] 
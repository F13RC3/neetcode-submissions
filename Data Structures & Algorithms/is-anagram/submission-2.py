class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = s.replace(" ",'').strip()
        t_ = t.replace(" ",'').strip()
        return sorted(s_) == sorted(t_)
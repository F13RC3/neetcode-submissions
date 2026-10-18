class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif not stack or stack.pop() != bracket_map[char]:
                return False
        if len(stack) == 0:
            return True
        return False
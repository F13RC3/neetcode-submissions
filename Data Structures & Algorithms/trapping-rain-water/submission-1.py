class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0]*n
        suffix = [0]*n
        tap_water = [0]*n

        current_max = 0
        for i in range(n):
            if height[i]>current_max:
                current_max = height[i]
            prefix[i] = current_max
        current_max = 0
        for i in range(n-1, -1, -1):
            if height[i]>current_max:
                current_max = height[i]
            suffix[i] = current_max

        for i in range(n):
            tap_water[i] = min(prefix[i], suffix[i])-height[i]
        
        return sum(tap_water)
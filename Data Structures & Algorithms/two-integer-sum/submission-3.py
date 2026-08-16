class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while i<len(nums)-1:
            difference = target - nums[i]
            if difference in nums[i+1:]:
                return [i,nums.index(difference, i+1)]
            i+=1
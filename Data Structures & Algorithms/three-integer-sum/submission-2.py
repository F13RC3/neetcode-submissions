class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j , k = i+1, len(nums)-1
            diff_target = 0 - nums[i]
            while j<k:
                sum = nums[j] + nums[k]
                if sum > diff_target:
                    k -= 1
                elif sum < diff_target:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j +=1
                    k-=1                
        return [list(triplets) for triplets in res]
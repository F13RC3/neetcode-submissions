class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j , k = i+1, len(nums)-1
            diff_target = 0 - nums[i]
            while j<k:
                sum = nums[j] + nums[k]
                if sum > diff_target:
                    k -= 1
                elif sum < diff_target:
                    j += 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    j +=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1      
        return res
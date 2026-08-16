class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num]=0
        sorted_values = sorted(res.items(),key=lambda item: item[1], reverse=True)
        return [val[0] for val in sorted_values[:k]]
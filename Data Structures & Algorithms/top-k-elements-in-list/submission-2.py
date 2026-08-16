class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for _ in range(len(nums)+1)]
        for num in nums:
            res[num] = res.get(num, 0) + 1
        for num, cnt in res.items():
            freq[cnt].append(num)

        final_res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                final_res.append(num)
                if len(final_res)==k:
                    return final_res
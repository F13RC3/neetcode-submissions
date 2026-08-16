class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for st in strs:
            key = "".join(sorted(st))
            if key in result:
                result[key].append(st)
            else:
                result[key] = [st]
        return list(result.values())
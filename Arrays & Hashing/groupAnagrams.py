class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key not in lists:
                lists[key] = []
            lists[key].append(s)
            
        return list(lists.values())

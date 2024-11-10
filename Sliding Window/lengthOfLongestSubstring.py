class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mapahash = dict()
        res = 0

        for r in range(len(s)):
            if s[r] in mapahash:
                l = max(mapahash[s[r]] + 1, l)
            mapahash[s[r]] = r
            res = max(res,r - l + 1)
        
        return res

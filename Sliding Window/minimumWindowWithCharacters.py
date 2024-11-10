class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count,found = dict(),dict()
        result, length = '', float("infinity")
        
        for i in t:
            count[i] = 1 + count.get(i, 0)

        have, need = 0, len(count)
        
        for r in range(len(s)):
            if s[r] in count:
                found[s[r]] = 1 + found.get(s[r], 0)
                if found[s[r]] == count[s[r]]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < length:
                    result = s[l : r + 1]
                    length = r - l + 1
                if s[l] in found:
                    found[s[l]] -= 1
                    if found[s[l]] < count[s[l]]:
                        have -= 1
                l += 1
        
        return result

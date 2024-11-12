class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            time = 0

            for i in piles:
                time += math.ceil(float(i) / m)
            
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res

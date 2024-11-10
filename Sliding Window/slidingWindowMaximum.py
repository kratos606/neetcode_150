class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        output = []
        q = deque()
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            while q and q[0] <= r - k:
                q.popleft()
            
            if r - l + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

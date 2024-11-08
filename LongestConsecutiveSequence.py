class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapahash = defaultdict(int)
        longest = 0
        
        for i in nums:
            if not mapahash[i]:
                left = mapahash[i - 1]
                right = mapahash[i + 1]
                length = left + right + 1

                mapahash[i] = length

                mapahash[i - left] = length
                mapahash[i + right] = length

                longest = max(longest, length)

        return longest


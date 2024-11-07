from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in frequency.items():
            bucket[freq].append(num)
        
        result = []

        for freq in range(len(bucket) - 1, 0, -1):
            if bucket[freq]:
                result.extend(bucket[freq])
                if len(result) >= k:
                    return result[:k]

        return result

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        
        for i, num in enumerate(nums):
            remainder = target - num
            
            if remainder in counter:
                return [counter[remainder], i]
            
            counter[num] = i

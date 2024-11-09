class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            result = self.twoSum(nums[i + 1:], -nums[i])
            if len(result) > 0:
                for pair in result:
                    triplet = [nums[i]] + pair
                    if triplet not in output:
                        output.append(triplet)
        return output

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        output = []
        while l < r:
            result = numbers[l] + numbers[r]
            if result > target:
                r -= 1
            elif result < target:
                l += 1
            else:
                output.append([numbers[l], numbers[r]])
                l += 1
                r -= 1
                while numbers[l] == numbers[l - 1] and l < r:
                    l += 1

        return output

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxes = []
        current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                maxes.append(current)
                current = 0   
        return maxes
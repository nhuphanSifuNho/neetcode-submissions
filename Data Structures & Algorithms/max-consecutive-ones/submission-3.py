class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxes = []
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                count +=1
            else:
                print(count)
                count = 0
        return max(maxes)

        
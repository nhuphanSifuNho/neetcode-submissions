class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums:
                j = nums.index(complement)
                if j != i:
                    return sorted([i, j])



                    
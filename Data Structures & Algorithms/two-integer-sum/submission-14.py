class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            elm = target - n
            if elm in nums:
                j = nums.index(elm)
                if j != i:
                    return sorted([i, j])
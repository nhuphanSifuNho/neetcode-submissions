class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while len(nums) > 0:
            if nums[i] == val:
                nums.remove(nums[i])
            i += 1
        return len(nums)
        
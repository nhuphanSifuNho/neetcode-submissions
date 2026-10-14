class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        reverse_arr = arr[::-1]
        result = []
        for i in range(1, len(reverse_arr) - 1):
            result.append(max(0, *reverse_arr[:i]))
        return result
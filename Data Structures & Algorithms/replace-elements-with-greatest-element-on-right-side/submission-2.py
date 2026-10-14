class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        reverse_arr = arr[::-1]
        result = []
        for i in range(len(reverse_arr) - 1):
            result.append(max(reverse_arr[:i]))
        return result
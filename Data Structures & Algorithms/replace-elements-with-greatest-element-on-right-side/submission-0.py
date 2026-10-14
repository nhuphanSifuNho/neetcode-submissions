class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[::-1]
        result = []
        for i in range(len(arr)):
            result.append(max(arr[:i]))
        return result
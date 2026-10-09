class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(1, len(arr)):
            result.append(max(0, *arr[i:]))
        result.append(-1)
        return result
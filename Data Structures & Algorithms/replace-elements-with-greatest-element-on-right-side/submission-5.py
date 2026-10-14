class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            result.append(max(0, *arr[i:]))
        return result
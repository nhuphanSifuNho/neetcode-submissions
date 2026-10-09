from typing import List

# Two pointers + swapping
def reverse_list(arr: List[int]) -> List[int]:
    ops = len(arr) // 2
    i = 0
    while i < ops:
        temp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = temp
        i += 1
    return arr

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

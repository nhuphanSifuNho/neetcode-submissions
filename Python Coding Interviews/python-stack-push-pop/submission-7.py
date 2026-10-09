from typing import List

# -- Loop Solutions --

# attemp1: wrong - iterating while removing
# def reverse_list(arr: List[int]) -> List[int]:
#     reverse_list = []
#     for elm in arr:
#         reverse_list.append(arr.pop())
#     return reverse_list

# Stack with while
# def reverse_list(arr: List[int]) -> List[int]:
#     # Define a stack
#     arr_reverse = []
    
#     while len(arr) > 0:
#         arr_reverse.append(arr.pop())
#     return arr_reverse
    
# Stack with for
# def reverse_list(arr: List[int]) -> List[int]:
#     stack = []
#     for _ in range(len(arr)):
#         stack.append(arr.pop())
#     return stack

# Stack with list comprehension
def reverse_list(arr: List[int]) -> List[int]:
    # list comprehension
    return [arr.pop() for _ in range(len(arr))]


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

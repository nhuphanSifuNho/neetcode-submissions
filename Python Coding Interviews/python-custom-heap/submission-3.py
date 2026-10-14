import heapq
from typing import List

# tuple-based max heap
def get_reverse_sorted(nums: List[int]) -> List[int]:
    # simulate heapify_max()
    pairs = [(-num, num) for num in nums]
    heapq.heapify(pairs)
    return [heapq.heappop(pairs)[1] for _ in range(len(pairs))]



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

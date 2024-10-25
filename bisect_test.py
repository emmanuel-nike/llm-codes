# import bisect

# # Create a sorted list
# sorted_list = [10, 20, 30, 40, 50]

# res = bisect.bisect_left(sorted_list, 21)  # Output will be 2
# print(res)
# sorted_list.insert(res, 21)
# print(sorted_list)  # Output will be [10, 20, 21, 30, 40, 50]

# res2 = bisect.bisect_right(sorted_list, 45)  # Output will be 2
# print(res2)
# sorted_list.insert(res2, 45)
# print(sorted_list)  # Output will be [10, 20, 21, 30, 40, 45, 50]

# # Insert a new element with bisect_left
# bisect.insort_left(sorted_list, 25)
# print(sorted_list)  # Output will be [10, 20, 25, 30, 40, 50]

# # Insert a new element with bisect_right
# bisect.insort_right(sorted_list, 30)
# print(sorted_list)  # Output will be [10, 20, 25, 30, 30, 40, 50]

# import heapq

# max_heap = []  # Left half (max-heap)
# min_heap = []  # Right half (min-heap)

# def insert(num):
#     # Insert into max_heap or min_heap accordingly to maintain order
#     if not max_heap or num <= -max_heap[0]:
#         heapq.heappush(max_heap, -num)  # Push the negative to simulate max-heap
#     else:
#         heapq.heappush(min_heap, num)

#     # Balance the heaps
#     if len(max_heap) > len(min_heap) + 1:
#         heapq.heappush(min_heap, -heapq.heappop(max_heap))
#     elif len(min_heap) > len(max_heap):
#         heapq.heappush(max_heap, -heapq.heappop(min_heap))

# # Example usage
# insert(3)
# insert(1)
# insert(5)
# insert(4)
# insert(22)
# insert(12)
# print(sorted([-x for x in max_heap] + min_heap))  # Output: [1, 3, 4, 5, 12, 22]

import numpy as np

arr = np.array([1, 2, 4, 5, 7, 9])
position = np.searchsorted(arr, 3)
arr = np.insert(arr, position, 3)
print(arr)  # Output: [1 2 3 4 5]

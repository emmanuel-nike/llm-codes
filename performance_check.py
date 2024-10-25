# import bisect
# import timeit
# import random

# # Setup a sorted list of a significant size
# size = 1000000
# sorted_list = list(range(size))

# # Function to insert using bisect
# def insert_with_bisect(sorted_list, value):
#     bisect.insort(sorted_list, value)

# # Function to insert using insert and sort
# def insert_with_insert_and_sort(sorted_list, value):
#     sorted_list.append(value)
#     sorted_list.sort()

# # Measure time for bisect insort
# bisect_time = timeit.timeit(
#     'insert_with_bisect(sorted_list, random.randint(0, size*2))',
#     globals=globals(),
#     number=1000
# )

# # Measure time for insert and sort
# insert_sort_time = timeit.timeit(
#     'insert_with_insert_and_sort(sorted_list, random.randint(0, size*2))',
#     globals=globals(),
#     number=1000
# )

# print(f"Bisect insort time: {bisect_time:.6f} seconds")
# print(f"Insert and sort time: {insert_sort_time:.6f} seconds")

# import bisect
# import random
# import timeit

# # Define the size of the list and the number of insertions
# list_size = 1000
# insertions = 1000

# #sorted_list = list(range(list_size))
# #print(sorted_list)

# # Generate a sorted list of random numbers
# sorted_list = sorted([random.randint(0, list_size) for _ in range(list_size)])
# print(sorted_list)

# # Define a function for inserting with bisect
# def insert_with_bisect(sorted_list, value):
#     bisect.insort(sorted_list, value)

# # Define a function for inserting with insert and sort
# def insert_with_insert_and_sort(sorted_list, value):
#     sorted_list.append(value)
#     sorted_list.sort()

# # Measure the time taken to perform insertions using bisect
# time_bisect = timeit.timeit(
#     'for i in range(insertions): insert_with_bisect(sorted_list, random.randint(0, list_size))',
#     globals=globals(),
#     number=1
# )

# # Measure the time taken to perform insertions using insert and sort
# time_insert_sort = timeit.timeit(
#     'for i in range(insertions): insert_with_insert_and_sort(sorted_list, random.randint(0, list_size))',
#     globals=globals(),
#     number=1
# )

# print(f"Time taken with bisect: {time_bisect:.6f} seconds")
# print(f"Time taken with insert and sort: {time_insert_sort:.6f} seconds")


# import bisect
# import random
# import timeit

# # Function using bisect
# def insert_with_bisect(sorted_list, value):
#     bisect.insort(sorted_list, value)

# # Function using insert and sort
# def insert_with_sort(sorted_list, value):
#     sorted_list.append(value)
#     sorted_list.sort()

# # Generate a large sorted list
# large_sorted_list = sorted(random.sample(range(1000000), 100000))

# # Value to insert
# value_to_insert = 50

# # Measure performance of bisect
# bisect_time = timeit.timeit(
#     'insert_with_bisect(large_sorted_list.copy(), value_to_insert)',
#     globals=globals(),
#     number=1000
# )

# # Measure performance of insert and sort
# sort_time = timeit.timeit(
#     'insert_with_sort(large_sorted_list.copy(), value_to_insert)',
#     globals=globals(),
#     number=1000
# )

# print(f"Time taken with bisect: {bisect_time:.6f} seconds")
# print(f"Time taken with insert and sort: {sort_time:.6f} seconds")


import bisect
import timeit

# Set up a large sorted list
large_list = list(range(1000000))

# Method using bisect module
def insert_with_bisect(sorted_list, value):
    bisect.insort(sorted_list, value)

# Method using insert and sort
def insert_and_resort(sorted_list, value):
    sorted_list.append(value)
    sorted_list.sort()

# Measure the time taken by bisect.insort
bisect_time = timeit.timeit(
    'insert_with_bisect(large_list, 560)',
    globals=globals(),
    number=100
)

# Measure the time taken by insert and sort
insert_resort_time = timeit.timeit(
    'insert_and_resort(large_list, 560)',
    globals=globals(),
    number=100
)

print(f"Time taken by bisect.insort: {bisect_time:.6f} seconds")
print(f"Time taken by insert and sort: {insert_resort_time:.6f} seconds")
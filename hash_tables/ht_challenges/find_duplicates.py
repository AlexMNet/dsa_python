"""
Given an array of integers nums, find all the duplicates in the array 
using a hash table (dictionary).

"""


def find_duplicates(nums):
    num_counts = {}

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    # List comprehension, creates a new array based on existing array
    duplicates = [num for num, count in num_counts.items() if count > 1]

    return duplicates


print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))  # [3, 4]

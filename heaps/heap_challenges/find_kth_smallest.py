from max_heap import MaxHeap

"""
  Udemy
Python Data Structures & Algorithms + LEETCODE Exercises
Heap: Kth Smallest Element in an Array
You are given a list of numbers called nums and a number k.

Your task is to write a function find_kth_smallest(nums, k) to find the kth smallest number in the list.

The list can contain duplicate numbers and k is guaranteed to be within the range of the length of the list.

This function will take the following parameters:

nums: A list of integers.

k: An integer.



This function should return the kth smallest number in nums.



Example 1:

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_smallest(nums, k))
In the example above, the function should return 2. If we sort the list, it becomes [1, 2, 3, 4, 5, 6]. The 2nd smallest number is 2, so the function returns 2.



Example 2:

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(find_kth_smallest(nums, k))
In the example above, the function should return 3. If we sort the list, it becomes [1, 2, 2, 3, 3, 4, 5, 5, 6]. The 4th smallest number is 3, so the function returns 3.

Note: For the purpose of this problem, we assume that duplicate numbers are counted as separate numbers. For example, in the second example above, the two 2s are counted as the 2nd and 3rd smallest numbers, and the two 3s are counted as the 4th and 5th smallest numbers.

"""


def find_kth_smallest(nums, k):
    heap = MaxHeap()

    for num in nums:
        heap.insert(num)
        if len(heap.heap) > k:
            heap.remove()

    return heap.remove()


print(find_kth_smallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # return 3
print(find_kth_smallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 7))  # return 5

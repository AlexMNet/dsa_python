"""
Max Heap

Rules
--------
1. Each node has a number higher than all its descendents. Highest number at the top!
2. Its a complete tree. Meaning tree is filled from left to right.
and each spot must be filled. 
3. Height of a tree is logN
4. Heaps can have duplicates (BST cannot)
5. Max heap has the highest value at the top
6. Min Heap has the is the inverse of the above
7. There is no particular order other than rule 1
8. Heaps are not good for searching. They are good for keeping track of the highest number and being able to remove it. 
9. Heaps will be stored in a list. List[num]

Equation for figuring out location of children (assuming list starting at 1)
- left_child = 2 * parent_index
- right_child = 2 * parent_index + 1

Equation for figuring out location of parent (assuming list starting at 1)
- Use integer division (chop off decimal). Divide child_index by 2 

*** Note that the MaxHeap implementation bellow will use the 0 index.
This means we must add 1 to left and right child equations and subract 1 (index -1) // 2 for the parent equestion
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)

        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        pass

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[index]:
                max_index = left_index

            if (
                right_index < len(self.heap)
                and self.heap[right_index] > self.heap[max_index]
            ):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
        pass

    # Only remove item from the top
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)

        return max_value

        pass


myheap = MaxHeap()
myheap.insert(99)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)

myheap.remove()

print(myheap.heap)

myheap.remove()

print(myheap.heap)

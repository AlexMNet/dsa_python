# Swap the values of the first and last node
# Method name swap_first_last
# Note that the pointers to the nodes themselves are not swapped - only their values are exchanged


def swap_first_last(self):
    if self.head is None or self.head == self.tail:
        return None
    
    self.head.value, self.tail.value = self.tail.value, self.head.value
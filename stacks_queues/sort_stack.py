# Stack: Sort Stack ( ** Interview Question)
# The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack.

# The function should use the pop, push, peek, and is_empty methods of the Stack object.

# Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.

# This will use the Stack class we created in these coding exercises:


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.empty():
            return None
        else:
            return self.stack_list.pop()


def sort_stack(input_stack):
    sorted_stack = Stack()

    while not input_stack.empty():
        temp = input_stack.pop()

        while not sorted_stack.empty() and sorted_stack.peek() > temp:
            input_stack.push(sorted_stack.pop())
        sorted_stack.push(temp)

    while not sorted_stack.empty():
        input_stack.push(sorted_stack.pop())


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

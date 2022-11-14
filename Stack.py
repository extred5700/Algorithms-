"""

Implementing a Python Stack without any libraries

Definition:
Stack is an abstract data type (ADT) that serves as a collection of elements with 2 main principal operations:
    1. Push - Adds an element to the element
    2. Pop - Removes the most recently added element that was not yet removed

Alternative name: LIFO (Last In First Out)
Diagram: 
|   Item 6  |
|   Item 5  |
|   Item 4  |
|   Item 3  |
|   Item 2  |
|   Item 1  |   Item 1 is pushed into the stack first, also meaning, in order to remove Item 1, 
-------------   we have to pop (remove) the rest of the items (Item 2 - 6) in order to remove Item 1 out from the stack

"""

# First example: Using a list to visualize it as a Stack
class Stack:
    # class attributes
    my_list_stack = []

    def add_element(self, element):
        self.my_list_stack += [element]

    def count_element(self):
        count = 0
        for element in self.my_list_stack:
            count += 1
        return count

    # Method to remove the last element of the stack by using the slice method
    def pop_element(self):
        if self.count_element == 0:
            print("Unable to pop element as the Stack is empty!")
        else:
            element_popped = self.my_list_stack[-1]
            self.my_list_stack = self.my_list_stack[:-1]
            return element_popped

""" Testing Codes """
# Using Class, no library 
print("\nStack using Class (NO LIBRARY)")
print("----------------------------------------------------------------")
# Create Stack object
stack_object = Stack()
print(f"Stack before pushing elements: {stack_object.my_list_stack}")

# Adding elements to the Stack
stack_object.add_element(100)
stack_object.add_element(1000)
stack_object.add_element(10000)
print(f"Stack after pushing elements: {stack_object.my_list_stack}")

# Check number of elements in a Stack
print(f"Number of elements in a Stack now: {stack_object.count_element()}")

# Removing elements from the Stack
print(f"Element from popping: {stack_object.pop_element()}")
print(f"Stack after popping: {stack_object.my_list_stack}")
print("----------------------------------------------------------------\n")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Using library functions 
print("\nStack using library")
print("----------------------------------------------------------------")
# Create stack object 
my_stack2 = []

# Adding elements to the Stack
my_stack2.append(200)
my_stack2.append(2000)
my_stack2.append(20000)
print(f"Stack after pushing elements: {my_stack2}")

# Check number of elements in a Stack
print(f"Number of elements in a Stack now: {len(my_stack2)}")

# Removing elements from the Stack
print(f"Element from popping: {my_stack2[-1]}")
my_stack2.pop()
print(f"Stack after popping: {my_stack2}")
print("----------------------------------------------------------------")
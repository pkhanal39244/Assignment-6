class Stack:
    # Initializes an empty stack
    def __init__(self):
        self.items = []

    # Pushes an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pops an item from the stack if not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    # Returns the top item of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # Checks if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Returns the size of the stack
    def size(self):
        return len(self.items)


class Queue:
    # Initializes an empty queue
    def __init__(self):
        self.items = []

    # Adds an item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Removes and returns the front item of the queue if not empty
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    # Returns the front item of the queue without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    # Checks if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Returns the size of the queue
    def size(self):
        return len(self.items)


class LinkedList:
    class Node:
        # Initializes a node with data and a reference to the next node
        def __init__(self, data=None):
            self.data = data
            self.next = None

    # Initializes an empty linked list
    def __init__(self):
        self.head = None

    # Appends a new node to the end of the linked list
    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Deletes a node with the given data from the linked list
    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    # Traverses and prints the linked list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Performance Analysis (Basic Operations)
def performance_analysis():
    # Stack Test
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack top: {stack.peek()}")
    stack.pop()
    print(f"Stack size after pop: {stack.size()}")

    # Queue Test
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue front: {queue.peek()}")
    queue.dequeue()
    print(f"Queue size after dequeue: {queue.size()}")

    # Linked List Test
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.traverse()
    linked_list.delete(2)
    linked_list.traverse()


if __name__ == "__main__":
    # Example usage for data structures
    performance_analysis()

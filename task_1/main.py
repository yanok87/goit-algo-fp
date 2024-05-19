"""Python program to reverse a linked list"""


# Node class
class Node:
    """Node class for Linked List"""

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class for Linked List"""

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        """Reverse Linked List function"""
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning
    def insert(self, new_data):
        """Add new Nodes to Liked List"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertion_sort(self):
        """Sort Linked List with insertion sort function"""
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        """Utility function to insert Nodes into sorted Linked List"""
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node

        current = sorted_list
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_list

        """Merging of the list with another Linked List"""
        dummy = Node(0)
        current = dummy
        list1 = self.head

        while list1 is not None and list2 is not None:
            if list1.data <= list2.head.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2.head
                list2.head = list2.head.next
            current = current.next

        current.next = list1 if list1 is not None else list2.head

        # Sort the merged list
        self.head = dummy.next
        self.insertion_sort()

    def print_list(self):
        """Utility function to print the Linked List"""
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Example usage:
list1 = LinkedList()
list1.insert(5)
list1.insert(1)
list1.insert(15)
list1.insertion_sort()
print("List1:")
list1.print_list()

list2 = LinkedList()
list2.insert(12)
list2.insert(4)
list2.insert(16)
list2.insertion_sort()
print("List2:")
list2.print_list()


def merge_sorted(l1, l2):
    """Merge two sorted linked lists"""
    # If one of the lists is empty, return the other list
    if not l1:
        return l2
    if not l2:
        return l1

    # Initialize merged list
    merged = LinkedList()

    # Set pointers to the heads of both lists
    current1 = l1.head
    current2 = l2.head

    # Traverse both lists and merge elements
    while current1 and current2:
        if current1.data < current2.data:
            merged.insert(current1.data)
            current1 = current1.next
        else:
            merged.insert(current2.data)
            current2 = current2.next

    # If any list has remaining elements, append them to the merged list
    while current1:
        merged.insert(current1.data)
        current1 = current1.next
    while current2:
        merged.insert(current2.data)
        current2 = current2.next

    # Reverse the merged list to get the correct order
    merged.reverse()

    return merged


# Example usage:
merged_list = merge_sorted(list1, list2)

# Print the merged list
current = merged_list.head
while current:
    print(current.data, end=" ")
    current = current.next

class Node:
    """
    A Node class representing each element in our linked list.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data    # The actual value stored in the node
        self.next = None    # Reference to the next node, initially None

class LinkedList:
    """
    LinkedList class that manages a collection of nodes.
    Provides methods for common operations like insertion, deletion, and traversal.
    """
    def __init__(self):
        """Initialize an empty linked list with no head node."""
        self.head = None
        self._size = 0  # Keep track of list size for O(1) length checking
    
    def insert_front(self, data):
        """
        Insert a new node at the beginning of the list.
        Time complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head  # Point new node to current head
        self.head = new_node       # Make new node the head
        self._size += 1
    
    def insert_end(self, data):
        """
        Insert a new node at the end of the list.
        Time complexity: O(n) where n is the length of the list
        """
        new_node = Node(data)
        
        # If list is empty, make new node the head
        if self.head is None:
            self.head = new_node
            self._size += 1
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self._size += 1
    
    def delete(self, data):
        """
        Delete the first occurrence of a node with the given data.
        Returns: True if node was found and deleted, False otherwise.
        Time complexity: O(n) where n is the length of the list
        """
        if self.head is None:  # Empty list
            return False
        
        # Special case: deleting head node
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True
        
        # Search for the node to delete
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Skip over the node to delete
                self._size -= 1
                return True
            current = current.next
            
        return False  # Data not found
    
    def find(self, data):
        """
        Search for a node with the given data.
        Returns: True if found, False otherwise.
        Time complexity: O(n)
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def __len__(self):
        """
        Return the length of the list.
        Time complexity: O(1) since we maintain a size counter
        """
        return self._size
    
    def __str__(self):
        """
        Create a string representation of the list.
        Useful for debugging and visualization.
        """
        if self.head is None:
            return "Empty list"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result + ["None"])

# Example usage with different Python data types
def example_usage():
    """Demonstrate various operations on the linked list."""
    # Create a new linked list
    lst = LinkedList()
    
    # Insert different types of data (Python's dynamic typing allows this!)
    lst.insert_front(42)          # integer
    lst.insert_end("Hello")       # string
    lst.insert_end([1, 2, 3])     # list
    lst.insert_front(3.14)        # float
    
    print("Initial list:", lst)
    print("List length:", len(lst))
    
    # Demonstrate deletion
    lst.delete("Hello")
    print("After deleting 'Hello':", lst)
    
    # Demonstrate search
    print("Is 42 in the list?", lst.find(42))
    print("Is 'Hello' in the list?", lst.find("Hello"))

if __name__ == "__main__":
    example_usage()
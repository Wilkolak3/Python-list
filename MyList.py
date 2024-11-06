class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class MyList:
    def __init__(self):
        self.head = None

    # dodaje element na koniec listy
    def add_element(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            element = self.head
            while element.next is not None:
                element = element.next
            element.next = node

    # wyświetla wszystkie elementy listy
    def display(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    # usuwa ostatni element listy
    def remove_element(self):
        if self.head is None:
            return
        node = self.head
        prev = None
        while node.next is not None:
            prev = node
            node = node.next
        if prev is not None:
            prev.next = None
        else:
            self.head = None

    # wyszukuje element o zadanej wartości
    def get_element(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return node
            node = node.next
        return None
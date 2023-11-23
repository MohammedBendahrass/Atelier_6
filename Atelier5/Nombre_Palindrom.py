class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def is_Palidrom(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values == values[::-1]


values = input("Entrez Les Valeurs de la liste séparées par des espaces : ").split()
head = Node(int(values[0]))
current = head
for value in values[1:]:
    current.next = Node(int(value))
    current = current.next
print(is_Palidrom(head))

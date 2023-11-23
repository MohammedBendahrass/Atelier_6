class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def move_to_the_first(head):
    if not head or not head.next:
        return head

    current = head
    perv = None

    while current.next:
        perv = current
        current = current.next

    perv.next = None
    current.next = head
    head = current
    return head


values = input("Entrez les valeurs de la liste séparées par des espaces : ").split()
head = Node(int(values[0]))
current = head

for value in values[1:]:
    current.next = Node(int(value))
    current = current.next

new_head = move_to_the_first(head)
current = new_head
while current:
    print(current.value, end=" ")
    current = current.next

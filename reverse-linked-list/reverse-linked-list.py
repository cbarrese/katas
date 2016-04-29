class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '%s %s' % (self.value, self.next)


def my_function(head):
    # write the body of your function here
    current = head
    previous = None
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return 'running with %s' % previous

# run your function through some test cases here
# remember: debugging is half the battle!
linkedList = LinkedListNode(0)
currentNode = linkedList
for i in range(5):
    currentNode.next = LinkedListNode(i+1)
    currentNode = currentNode.next

print my_function(linkedList)

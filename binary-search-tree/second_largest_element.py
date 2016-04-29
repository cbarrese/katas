class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def find_right_most_element(treenode):
    if not treenode.right:
        return treenode
    else:
        return find_right_most_element(treenode.right)


def find_second_largest_element(treenode):
    if not treenode.left:
        right_most_element = find_right_most_element(treenode)
        return right_most_element.parent.value
    else:
        right_most_element = find_right_most_element(treenode.left)
        return right_most_element.value

root_node = BinaryTreeNode(7)
left_node = root_node.insert_left(3)
left_node.insert_left(2)
left_node.insert_right(6)

right_node = root_node.insert_right(15)
right_node.insert_left(10)
right_node.insert_right(20)

print find_second_largest_element(root_node)

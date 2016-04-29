class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_binary_search_tree(treenode, bounds):
    if not treenode:
        return True
    elif treenode.value > bounds[1] or treenode.value < bounds[0]:
        return False
    else:
        return is_binary_search_tree(treenode.left, (bounds[0], treenode.value)) \
               and is_binary_search_tree(treenode.right, (treenode.value, bounds[1]))


root_node = BinaryTreeNode(7)
left_node = root_node.insert_left(3)
left_node.insert_left(2)
left_node.insert_right(6)

right_node = root_node.insert_right(15)
right_node.insert_left(10)
right_node.insert_right(20)

print is_binary_search_tree(root_node, (float('-inf'), float('+inf')))

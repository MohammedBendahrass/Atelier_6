class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def are_Cousins(root, x, y):
    def get_Depth_and_Parent(node, target, parent, depth):
        if not node:
            return None

        if node.value == target:
            return (depth, parent)

        result_left = get_Depth_and_Parent(node.left, target, node, depth + 1)
        result_right = get_Depth_and_Parent(node.right, target, node, depth + 1)

        return result_left or result_right

    result_x = get_Depth_and_Parent(root, x, None, 0)
    result_y = get_Depth_and_Parent(root, y, None, 0)

    if result_x and result_y:
        depth_x, parent_x = result_x
        depth_y, parent_y = result_y
        return depth_x == depth_y and parent_x != parent_y

    return False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(are_Cousins(root, 4, 6))
print(are_Cousins(root, 4, 7))
print(are_Cousins(root, 5, 6))
print(are_Cousins(root, 5, 7))
print(are_Cousins(root, 4, 5))
print(are_Cousins(root, 2, 3))
print(are_Cousins(root, 3, 4))
print(are_Cousins(root, 3, 5))
print(are_Cousins(root, 1, 5))
print(are_Cousins(root, 2, 5))

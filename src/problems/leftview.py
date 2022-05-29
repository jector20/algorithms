from datastructures import heap


def layerleft(root, depth):
    if root is None:
        return root
    if depth == 0:
        return root

    left = layerleft(root.left, depth-1)
    if left:
        return left

    left = layerleft(root.right, depth-1)
    if left:
        return left

    return None


def lefttree(node):
    height = heap.tree_height(node)

    for i in range(height):
        yield layerleft(node, i)


def leftview(root):

    if root is None:
        return []

    return [node.val for node in lefttree(root)]

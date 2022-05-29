

class MinHeap():
    pass


class MaxHeap():
    pass


def tree_height(root):
    h = 0

    if root:
        h += 1

        if root.left and root.right:
            h += max(tree_height(root.left), tree_height(root.right))
        elif root.left:
            h += tree_height(root.left)
        elif root.right:
            h += tree_height(root.right)
        else:
            pass

    return h


def tree_height(root):
    h = 0

    if root:
        h += 1

        if root.left and root.right:
            h += max(tree_height(root.left), tree_height(root.right))
        elif root.left:
            h += tree_height(root.left)
        elif root.right:
            h += tree_height(root.right)
        else:
            pass

    return h

from typing import Optional
from datastructures import TreeNode


def structure(root):
    """
    Same as BFS result for a tree
    """
    queue = [root]

    while queue:
        n = queue.pop()
        if n:
            queue.append(n.left if n.left else None)
            queue.append(n.right if n.right else None)

        yield n


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    node_p = structure(p)
    node_q = structure(q)

    for n1, n2 in zip(node_p, node_q):
        if n1 is None and n2 is None:
            continue

        if n1 and n2 and n1.val == n2.val:
            continue

        return False

    return True

from typing import Optional
from datastructures import TreeNode


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is not None and q is not None:
        if p.val == q.val:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        else:
            return False
    elif p is None and q is None:
        return True

    return False

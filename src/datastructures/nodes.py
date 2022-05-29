from functools import reduce
from itertools import islice


class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode():

    def __init__(self, val):
        self.val = val
        self.next = None


def cycle_linkedlist_nodes(nodes, position):
    head = [ListNode(n) for n in nodes]

    def link(lst, node):
        lst.next = node
        return node

    reduce(link, head)

    if position >= 0:
        head[-1].next = head[position]

    return head[0] if len(head) > 0 else None


def tree_nodes(tree_str):

    def binaryNode(data):
        return TreeNode(int(data)) if data != 'N' else None

    if tree_str == '':
        return None

    tree_array = tree_str.split(' ')
    nodes = list(map(binaryNode, tree_array))

    node_count = len(nodes)
    for i in range(node_count):
        left = 2 * i + 1
        right = 2 * i + 2
        if nodes[i]:
            if left < node_count and nodes[left]:
                nodes[i].left = nodes[left]
            if right < node_count and nodes[right]:
                nodes[i].right = nodes[right]

    return nodes[0]

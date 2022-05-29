from typing import Optional
from datastructures import ListNode


def node_list(group_start, group_end=None):
    while group_start != group_end:
        yield group_start
        group_start = group_start.next
    if group_start is not None:
        yield group_start


def has_cycle(head: Optional[ListNode]) -> bool:
    group = None
    group_append = None
    for node in node_list(head):
        for safe in node_list(group, group_append):
            if node.next == safe:
                return True
        if group is None:
            group = group_append = node
        else:
            group_append = node

    return False

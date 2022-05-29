from typing import Optional
from datastructures import ListNode


def node_list(group_start, group_end=None):
    while group_start != group_end:
        yield group_start
        group_start = group_start.next
    if group_start is not None:
        yield group_start


def has_cycle(head: Optional[ListNode]) -> bool:

    safe = set()
    for node in node_list(head):
        if node.next in safe:
            return True
        safe |= set([node])

    return False

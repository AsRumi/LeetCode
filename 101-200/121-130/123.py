"""
Note on sorting a linked list using merge sort.
"""

def merge(head1, head2):
    # Since both lists are sorted from the sort_list() call, 
    # write the merging logic here. The same one from the previous file.
    return None

def sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next        # first-middle variant
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid, slow.next = slow.next, None    # CUT the list in two
    return merge(sort_list(head), sort_list(mid))
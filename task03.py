from linked_list import ListNode, build_list, to_list


def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def build_with_cycle(values, pos):
    head = build_list(values)
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    if pos >= 0 and nodes:
        nodes[-1].next = nodes[pos]
    return head


if __name__ == "__main__":
    print(has_cycle(build_with_cycle([3, 2, 0, -4], 1)))
    print(has_cycle(build_with_cycle([1, 2], 0)))
    print(has_cycle(build_with_cycle([1], -1)))

from linked_list import ListNode, build_list, to_list


def reorder_list(head):
    if not head or not head.next:
        return
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    previous = None
    while second:
        following = second.next
        second.next = previous
        previous = second
        second = following
    first, second = head, previous
    while second:
        first_next = first.next
        second_next = second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next


if __name__ == "__main__":
    for values in ([1, 2, 3, 4], [1, 2, 3, 4, 5]):
        head = build_list(values)
        reorder_list(head)
        print(to_list(head))

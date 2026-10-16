from linked_list import ListNode, build_list, to_list


def partition(head, x):
    small_dummy = ListNode()
    large_dummy = ListNode()
    small = small_dummy
    large = large_dummy
    while head:
        following = head.next
        head.next = None
        if head.val < x:
            small.next = head
            small = head
        else:
            large.next = head
            large = head
        head = following
    small.next = large_dummy.next
    return small_dummy.next


if __name__ == "__main__":
    print(to_list(partition(build_list([1, 4, 3, 2, 5, 2]), 3)))
    print(to_list(partition(build_list([2, 1]), 2)))

from linked_list import ListNode, build_list, to_list


def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next
        group_next = kth.next
        prev = group_next
        current = group_prev.next
        while current is not group_next:
            following = current.next
            current.next = prev
            prev = current
            current = following
        old_start = group_prev.next
        group_prev.next = kth
        group_prev = old_start


if __name__ == "__main__":
    print(to_list(reverse_k_group(build_list([1, 2, 3, 4, 5]), 2)))
    print(to_list(reverse_k_group(build_list([1, 2, 3, 4, 5]), 3)))

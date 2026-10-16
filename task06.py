from linked_list import ListNode, build_list, to_list


def double_it(head):
    if head is None:
        return None
    if head.val >= 5:
        head = ListNode(0, head)
    current = head
    while current:
        current.val = (current.val * 2) % 10
        if current.next and current.next.val >= 5:
            current.val += 1
        current = current.next
    return head


if __name__ == "__main__":
    print(to_list(double_it(build_list([1, 8, 9]))))
    print(to_list(double_it(build_list([9, 9, 9]))))

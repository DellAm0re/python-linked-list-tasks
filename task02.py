from linked_list import ListNode, build_list, to_list


def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


if __name__ == "__main__":
    print(to_list(delete_duplicates(build_list([1, 1, 2]))))
    print(to_list(delete_duplicates(build_list([1, 1, 2, 3, 3]))))

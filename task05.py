from linked_list import ListNode, build_list, to_list


def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == "__main__":
    head = build_list([4, 5, 1, 9])
    delete_node(head.next)
    print(to_list(head))
    head = build_list([4, 5, 1, 9])
    delete_node(head.next.next)
    print(to_list(head))

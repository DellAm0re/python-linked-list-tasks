from linked_list import ListNode, build_list, to_list


def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next


if __name__ == "__main__":
    print(to_list(merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))))
    print(to_list(merge_two_lists(build_list([]), build_list([]))))
    print(to_list(merge_two_lists(build_list([]), build_list([0]))))

from linked_list import ListNode, build_list, to_list


import heapq


def merge_k_lists(lists):
    heap = []
    for index, node in enumerate(lists):
        if node is not None:
            heapq.heappush(heap, (node.val, index, node))
    dummy = ListNode()
    tail = dummy
    while heap:
        _, index, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, index, node.next))
    tail.next = None
    return dummy.next


if __name__ == "__main__":
    print(to_list(merge_k_lists([build_list(a) for a in [[1, 4, 5], [1, 3, 4], [2, 6]]])))
    print(to_list(merge_k_lists([])))
    print(to_list(merge_k_lists([build_list([])])))

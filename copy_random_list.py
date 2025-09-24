# copy_random_list.py
# ---------------------------------------------------------
# Problem: Copy List with Random Pointer (LeetCode 138)
#
# A linked list is given where each node contains:
#   - val: an integer value
#   - next: pointer to the next node
#   - random: pointer to any node in the list (or None)
#
# Task: Construct a deep copy of the list and return the
#       head of the copied list.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------

from typing import Optional


class Node:
    def __init__(self, val: int = 0, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random

    def __repr__(self):
        # Display value and random for easier debugging
        random_val = self.random.val if self.random else None
        return f"Node(val={self.val}, random={random_val})"


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Insert copied nodes after original nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers for copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the original and copied lists
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next

        return copy_head


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    # Build a sample linked list: 1 -> 2 -> 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next, node2.next = node2, node3

    # Random pointers
    node1.random = node3  # 1 → 3
    node2.random = node1  # 2 → 1
    node3.random = node2  # 3 → 2

    print("Original list:")
    curr = node1
    while curr:
        print(curr)
        curr = curr.next

    # Deep copy
    solution = Solution()
    copied_head = solution.copyRandomList(node1)

    print("\nCopied list:")
    curr = copied_head
    while curr:
        print(curr)
        curr = curr.next

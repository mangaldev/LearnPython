# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        size = 0
        while temp:
            size = size + 1
            temp = temp.next

        result = [0] * size
        stack = []
        index = -1

        while head:
            index += 1
            current = head.val
            while stack and stack[-1][1] < current:
                result[stack[-1][0]] = current
                stack.pop()
            stack.append((index, current))
            head = head.next

        return result

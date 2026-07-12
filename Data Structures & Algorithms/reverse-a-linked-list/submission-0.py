# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        root = head

        stack = []

        while root:
            stack.append(root)
            root = root.next

        head = stack.pop(-1)
        prev = head
        prev.next = None

        while stack:
            curr = stack.pop(-1)
            prev.next = curr
            prev = curr
            prev.next = None
        return head
        


        
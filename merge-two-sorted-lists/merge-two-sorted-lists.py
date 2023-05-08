# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize the result linked list
        dummy = ListNode(0)
        curr = dummy
        
        # Traverse both input linked lists simultaneously
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Append the remaining nodes from list1 or list2
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        # Return the head of the merged linked list
        return dummy.next
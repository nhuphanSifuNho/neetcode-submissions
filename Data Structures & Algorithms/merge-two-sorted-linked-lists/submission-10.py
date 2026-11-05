# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy list node
        dummy = ListNode(-1)
        # 2. Access the dummy list node
        curr = dummy
        # 3. Traverse both node lists
        while list1 and list2:
            # 4. Compare the val of the current item in each node list
            if list1.val <= list2.val:
                # 5a. Point to that node list1 because its val is lower
                curr.next = list1
                # 6b. Move to the next node in list1
                list1 = list1.next
            else:
                # 5b. Point to that node in list2 becuase its val is lower
                curr.next = list2
                # 6b. Move to the next node in lit2
                list2 = list2.next
            # 7. Move to the next curr
            curr = curr.next
        # 8. Leftover nodes
        curr.next = list1 if list1 else list2
        return dummy.next
        

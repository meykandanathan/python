class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

l1_input = list(map(int, input("Enter the values for first linked list, separated by spaces: ").strip().split()))
l2_input = list(map(int, input("Enter the values for second linked list, separated by spaces: ").strip().split()))

l1 = ListNode(l1_input[0])
l1_curr = l1
for i in range(1, len(l1_input)):
    l1_curr.next = ListNode(l1_input[i])
    l1_curr = l1_curr.next

l2 = ListNode(l2_input[0])
l2_curr = l2
for i in range(1, len(l2_input)):
    l2_curr.next = ListNode(l2_input[i])
    l2_curr = l2_curr.next

result = mergeTwoLists(l1, l2)

print("Merged Linked List:")
while result:
    print(result.val, end=" ")
    result = result.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
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

'''
На каждом шаге tail.next указывает на меньший из текущих узлов list1 и list2, после чего соответствующий указатель сдвигается вперёд. 
В конце оставшаяся часть одного списка просто присоединяется к tail.next, поэтому слияние сохраняет порядок и требует только константное число указателей.
'''
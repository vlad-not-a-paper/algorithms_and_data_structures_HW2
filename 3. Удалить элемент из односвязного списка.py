class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(0, head)
    current = dummy
    
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
            
    return dummy.next

'''
Случаи удаления головы и внутренних элементов обрабатываются единообразно благодаря фиктивному узлу dummy, который стоит перед head. 
Указатель current всегда указывает на узел перед удаляемым. Чтобы удалить узел, мы перезаписываем ссылку current.next = current.next.next, 
перепрыгивая через него. Если удаляется голова, dummy играет роль предыдущего узла, и возврат dummy.next корректно обновляет начало списка.
'''
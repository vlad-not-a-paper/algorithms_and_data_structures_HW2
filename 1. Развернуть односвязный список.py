class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev

'''
На каждом шаге мы сохраняем следующий узел, разворачиваем ссылку текущего узла на предыдущий и сдвигаем указатели prev и current вперед. 
Когда current становится None, prev указывает на новый первый узел. 
Алгоритм работает за O(n), потому что цикл выполняется ровно n раз, а внутри цикла совершаются только константные операции.
'''
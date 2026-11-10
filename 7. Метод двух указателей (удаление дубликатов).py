def removeDuplicates(nums):
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

'''
Медленный указатель slow отмечает позицию последнего уникального элемента, быстрый fast ищет следующий отличный от него. 
Когда fast находит новый уникальный элемент, мы увеличиваем slow и записываем туда nums[fast]. 
Все дубликаты, находящиеся между slow и fast, затираются этим новым значением, поэтому дополнительная память не нужна.
'''
def twoSumSorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

'''
Метод работает за O(n), потому что на каждой итерации мы либо увеличиваем left, либо уменьшаем right. 
Сумма nums[left] + nums[right] монотонно зависит от указателей: если она меньше target, то единственный способ её увеличить - сдвинуть left вправо; 
если больше - сдвинуть right влево. Поэтому мы не пропускаем возможную пару и делаем не более n шагов.
'''
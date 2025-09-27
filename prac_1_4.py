# задача 5
n = int(input('Укажите, до какого числа выполнять проверку: '))
nums = [i for i in range(2, n + 1)]
for num in nums:
    for i in nums[nums.index(num)+1:]:
        if i % num == 0:
            nums.pop(nums.index(i))
print(f'Вот все простые числа от 2 до {n}:')
print(nums)
